from abc import ABC, abstractmethod
import json
from urllib.parse import urlencode
from collections.abc import Iterable

import httplib2

from .types import BaseType, Error
from .services import fix_built_ins


class BaseMethod(ABC):
    request_url = 'https://api.telegram.org/bot'

    http_method = 'GET'
    response_type = BaseType

    content_type = 'application/json'
    success_http_statuses = [200]

    @abstractmethod
    def __init__(self, *, propagate_values=False, propagate_fields=None):
        self.method_name = self.__class__.__name__
        self.propagate_values = propagate_values
        self.propagate_fields = propagate_fields
        self.token = None

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

    def get_method_url(self):
        """Generate url for calling method api."""
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
        else:
            return urlencode(data)

    def execute(self):
        """Send method request."""
        assert hasattr(self, 'token'), 'Bot token must be provided for method execution.'

        headers = {
            'content-type': self.content_type
        }

        http = httplib2.Http()
        resp, content = http.request(self.get_method_url(), method=self.http_method, body=self.get_method_body(),
                                     headers=headers)
        if int(resp['status']) not in self.success_http_statuses:
            return self.parse_response(content, Error)
        return self.parse_response(content)

    def parse_response(self, response, response_type=None):
        # Parse response and return once of available response types.

        response = json.loads(response)
        if isinstance(self.response_type, Iterable) and not response_type:
            # If response type have a kind [response_type,] for multiple responses.
            self.response_type = self.response_type[0]
            return [self.response_type(**fix_built_ins(result)) for result in response['result']]
        else:
            return self.response_type(**fix_built_ins(response['result'])) if not response_type else response_type(**response)






