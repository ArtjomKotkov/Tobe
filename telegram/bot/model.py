import os


class BaseBot:

    def __init__(self, name=None, token=None):
        self.token = token
        self.name = name

    def set_name(self, name:str):
        self.name = name

    def set_token(self, token:str):
        self.token = token

    def get_token(self):
        return self.token

class BotTemplate:
    """Provide basic bot creating interface."""

    def __init__(self, name_key:str=None):
        """
        :param name_key: key for generating temporary bot name.
        """
        self.name_key = name_key
        super().__init__(name=BotTemplate.gen_name(self.name_key))

    @staticmethod
    def gen_name(name_key):
        """Generate name of bot by name_key."""
        ending = os.urandom(10).hex()
        return name_key+ending if name_key else ending

