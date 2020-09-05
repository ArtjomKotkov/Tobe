from collections.abc import Iterable

from ..methods import BaseMethod, getMe


class Bot:
    """Main bot class."""

    def __init__(self, token=None):
        self.token = token

    def set_token(self, token:str):
        self.token = token

    def get_token(self):
        return self.token

    def sync(self):
        for key, value in self.execute(getMe()).__dict__.items():
            setattr(self, key, value)
        return self

    def execute(self, cmd, forced=False):
        """Execution command(s).

        Parameters
        ----------
            cmd: instance(BaseMethod) or Iterable of BaseMethod instances.
                List of command which need's to execute.
            forced: bool
                If forced=True, skip failed executions if commands were acquired as list of methods.
                If forced=false, if get failed execution, stop send next commands.
        """

        result = None # Result of execution, iterable or type instance.

        assert isinstance(cmd, Iterable) or isinstance(
            cmd, BaseMethod), 'cmd must be instance of BaseMethod or iter of BaseMethod.'

        if isinstance(cmd, Iterable):
            result = []
            for num, method in enumerate(cmd):
                    if forced:
                        response = method.set_token(self.get_token()).execute()
                        result.append(response)
                    else:
                        response = method.set_token(self.get_token()).execute()
                        result.append(response)
                        if response.status == False:
                            break
        else:
            result = cmd.set_token(self.get_token()).execute()
        return result

