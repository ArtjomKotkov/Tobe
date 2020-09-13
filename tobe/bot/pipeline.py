from .methods import BaseMethod


class Pipe:

    def __init__(self, method: BaseMethod, load_fields: dict = None, skip_answer=False, load_from: int = None):
        self.method = method
        self.load_fields = load_fields
        self.skip_answer = skip_answer
        self.load_from = load_from

    def execute(self):
        if self.load_from:
            data = self.tmp_stash.get(
                self.load_from) if self.load_from > 1 or self.load_from <= self.counter - 1 else self.tmp_stash.get(
                self.counter - 1)
            self.method.propagate_from_dict(data)
        return {self.counter: self.method.execute()}

    def tmp_stash(self, dict: dict):
        self.tmp_stash = dict
        return self

    def set_token(self, token: str):
        self.method.set_token(token)
        return self

    def set_counter(self, counter: int):
        self.counter = counter
        return self
