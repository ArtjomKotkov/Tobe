from abc import ABC
import json

from .services import fix_built_ins


class BaseType(ABC):

    status = True

    def serialize(self):
        return json.dumps(self.__dict__)

    @classmethod
    def parse(cls, response, iterable=False):
        """Parse data from response, fix built in names

            Returns:
                Type instance.
        """
        if iterable:
            return [cls(**fix_built_ins(part)) for part in response] if response else None
        else:
            return cls(**fix_built_ins(response)) if response else None

class Error(BaseType):
    """Error type class."""

    status = False

    def __init__(self, ok, error_code, description):
        self.status = ok
        self.error_code = error_code
        self.description = description