from abc import ABC, abstractmethod
import json
from collections.abc import Iterable

import requests
import httplib2

from .types import BaseType, Error
from .services import fix_built_ins
from .base.types import InputFile


class BaseMethod(ABC):
    request_url = 'https://api.telegram.org/bot'

    http_method = 'GET'
    response_type = BaseType

    content_type = 'application/json'
    success_http_statuses = [200]

    @abstractmethod
    def __init__(self, *, propagate_values=False, propagate_fields=None, headers=None):
        self.method_name = self.__class__.__name__
        self.propagate_values = propagate_values
        self.propagate_fields = propagate_fields
        self.token = None
        try:
            self.headers = {}.update(headers)
        except TypeError:
            self.headers = {}

    def set_token(self, token):
        self.token = token
        return self

    def serialize(self):
        return json.dumps(self.__dict__)

    def propagate_from_bot(self, bot_instance):
        """Load attrs from provided bot instance."""
        self.token = bot_instance.token
        for key in self.__dict__.keys():
            try:
                setattr(self, key, bot_instance.propagated_values[key])
            except KeyError:
                pass
        return self

    def propagate_from_dict(self, dict: dict):

        for key, value in dict.values():
            setattr(self, key, value)
        return self

    def get_method_url(self):
        """Generate url for calling method api."""
        print(self.request_url, self.token, self.method_name)
        return self.request_url + self.token + '/' + self.method_name

    def get_method_body(self):
        """Generate request body for calling method api."""

        data = dict(self.__dict__)
        data.pop('token')
        data.pop('propagate_values')
        data.pop('method_name')
        blank_keys = []
        for key, value in data.items():
            if not value:
                blank_keys.append(key)
        for key in blank_keys:
            data.pop(key)
        if self.http_method == 'GET':
            return json.dumps(data)
        elif self.http_method == 'POST':
            return data

    def execute(self):
        """Send method request."""
        assert hasattr(self, 'token'), 'Bot token must be provided for method execution.'

        headers = {
            'content-type': self.content_type
        }.update(self.headers)

        if self.http_method == 'GET':
            resp = requests.post(url=self.get_method_url(), data=self.get_method_body(),
                                headers=headers)

            print(resp.request.body)
        elif self.http_method == 'POST':
            data, files = self.get_method_body()
            resp = requests.post(url=self.get_method_url(), data=data, files=files, headers=headers)

        if int(resp.status_code) not in self.success_http_statuses:
            return self.parse_response(resp.json(), Error)
        return self.parse_response(resp.json())

    def parse_response(self, response, response_type=None):
        # Parse response and return once of available response types.

        if isinstance(self.response_type, Iterable) and not response_type:
            # If response type have a kind [response_type,] for multiple responses.
            self.response_type = self.response_type[0]
            return [self.response_type(**fix_built_ins(result)) for result in response['result']]
        else:
            return self.response_type(**fix_built_ins(response['result'])) if not response_type else response_type(
                **response)


class FileMethod:
    file_class = None
    file_response_class = None

    def load_file(self, file_or_str):
        if isinstance(file_or_str, InputFile):
            return file_or_str.file
        elif isinstance(file_or_str, self.file_class):
            return file_or_str.media
        elif isinstance(file_or_str, self.file_response_class):
            return file_or_str.file_id
        else:
            raise TypeError(
                f'Only InputFile, {self.file_class.__name__}, {self.file_response_class.__name__} are available.')
