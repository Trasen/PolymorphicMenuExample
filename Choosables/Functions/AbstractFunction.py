import abc
from Choosables.Choosable import Choosable


class AbstractFunction(Choosable):

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def choice(cls, previous_menu: Choosable, userinput: int) -> Choosable:
        return cls.get_previous_choosable()

    @classmethod
    @abc.abstractmethod
    def execute(cls):
        pass
