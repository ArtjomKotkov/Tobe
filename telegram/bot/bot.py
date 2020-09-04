from collections.abc import Iterable

from .model import BaseBot
from ..methods import BaseMethod


class Bot(BaseBot):
    """Main bot class."""

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
        assert isinstance(cmd, Iterable) or isinstance(
            cmd, BaseMethod), 'cmd must be instance of BaseMethod or iter of BaseMethod.'

        if isinstance(cmd, Iterable):
            status = True
            for num, method in enumerate(cmd):
                    if forced:
                        method.get_token(self.get_token()).execute()
                    elif status == True:
                        status = method.get_token(self.get_token()).execute()
                    else:
                        return exe






