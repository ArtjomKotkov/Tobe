from abc import ABC, abstractmethod
import json


class ResponseBaseType(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def serialize(self):
        return json.dumps(self.__dict__)
