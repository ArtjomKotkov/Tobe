from collections.abc import Iterable

from ..methods import BaseMethod, getMe
from ..decorators import propagate_value


class Bot:
    """Main bot class."""

    def __init__(self, token=None):
        self.token = token
        self.propagated_values = {}

    def set_token(self, token:str):
        self.token = token

    def get_token(self):
        return self.token

    def sync(self):
        for key, value in self.execute(getMe()).__dict__.items():
            setattr(self, key, value)
        return self

    @propagate_value(update_id='offset')
    def execute(self, cmd, forced=False, propogate=False):
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
                    # If global propogate is enabled.
                    method.set_token(self.get_token())
                    if propogate:
                        method = method.propagate_from_bot(self)
                    elif method.propagate_values:
                        method = method.propagate_from_bot(self)
                    if forced:
                        response = method.execute()
                        result.append(response)
                    else:
                        response = method.execute()
                        result.append(response)
                        if response.status == False:
                            break
        else:
            cmd.set_token(self.get_token())
            if propogate:
                cmd = cmd.propagate_from_bot(self)
            elif cmd.propagate_values:
                cmd = cmd.propagate_from_bot(self)
            result = cmd.execute()
        return result[0] if isinstance(result, Iterable) and len(result) == 1 else result

