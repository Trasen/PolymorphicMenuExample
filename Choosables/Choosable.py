from __future__ import annotations

import abc


class Choosable(metaclass=abc.ABCMeta):

    previous_choice: Choosable

    @classmethod
    @abc.abstractmethod
    def choice(cls, choosable, input: int) -> Choosable:
        pass

    @classmethod
    @abc.abstractmethod
    def execute(cls):
        pass

    @classmethod
    @abc.abstractmethod
    def to_string(cls) -> str:
        pass

    @classmethod
    def set_previous_choosable(cls, choosable: Choosable) -> None:
        cls.previous_choice = choosable

    @classmethod
    def get_previous_choosable(cls) -> Choosable:
        return cls.previous_choice
