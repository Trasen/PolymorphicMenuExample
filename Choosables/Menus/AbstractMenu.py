import abc

from Choosables.Choosable import Choosable
from Choosables.Functions.AbstractFunction import AbstractFunction


class AbstractMenu(Choosable):
    choosables = list()

    @classmethod
    @abc.abstractmethod
    def __init__(cls, listofchoosables):
        cls.choosables = listofchoosables

    @classmethod
    def choice(cls, previous_menu: Choosable, userinput: int) -> Choosable:
        cls.set_previous_choosable(previous_menu)
        userchoice: Choosable = cls.choosables.__getitem__(userinput)()
        userchoice.set_previous_choosable(cls)

        if isinstance(userchoice, AbstractFunction):
            userchoice.execute()
            return cls
        else:
            return userchoice

    @classmethod
    def execute(cls) -> None:
        i = 0
        for choice in cls.choosables:
            print(str(i) + " : " + choice.to_string())
            i += 1

    @classmethod
    @abc.abstractmethod
    def to_string(cls) -> str:
        pass
