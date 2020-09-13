from collections.abc import Iterable

from .methods import BaseMethod
from .base.methods import getMe
from .decorators import propagate_value
from .pipeline import Pipe


class Bot:
    """Main bot class."""

    def __init__(self, token=None):
        self.token = token
        self.propagated_values = {}

    def set_token(self, token: str):
        self.token = token

    def get_token(self):
        return self.token

    def sync(self):
        for key, value in self.execute(getMe()).__dict__.items():
            setattr(self, key, value)
        return self

    def clear_cache(self):
        self.propagated_values = {}

    def get_propagate_value(self, key: str):
        return self.propagated_values.get(key, None)

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
            progate_fields: dict
                Fields which need to propogate into the bot (for saving it for next request).
                User key=value syntax, where key - field from method, value - field to bot.
                Supports inherit strictures, like - 'message.chat.id'.
        """

        result = None  # Result of execution, iterable or type instance.

        assert isinstance(cmd, Iterable) or isinstance(
            cmd, BaseMethod), 'cmd must be instance of BaseMethod or iter of BaseMethod.'

        if isinstance(cmd, Iterable):
            result = []
            for num, method in enumerate(cmd):
                # Propagating files.
                method.set_token(self.get_token())
                if propogate or method.propagate_values:
                    method = method.propagate_from_bot(self)
                if forced:
                    response = method.execute()
                    result.append((response, method.propagate_fields))
                else:
                    response = method.execute()
                    result.append((response, method.propagate_fields))
                    try:
                        if response.status == False:
                            break
                    except AttributeError:
                        pass
        else:
            cmd.set_token(self.get_token())
            if propogate or cmd.propagate_values:
                cmd = cmd.propagate_from_bot(self)
            result = (cmd.execute(), cmd.propagate_fields)
        return result[0] if isinstance(result, Iterable) and len(result) == 1 else result

    def pipeline(self, *args, return_tmp=False):

        tmp_answers = {}

        pipe_counter = 0

        for pipe in args:
            if isinstance(pipe, Pipe):
                pipe.set_token(self.get_token())
                pipe.tmp_stash(tmp_answers)
                pipe.set_counter(pipe_counter)

                tmp_answers.update(pipe.execute())

                pipe_counter += 1

        return [value for value in tmp_answers.values()] if return_tmp else None
