import abc
from functools import singledispatchmethod

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

        return cls.rule(userchoice)

    @singledispatchmethod
    @classmethod
    def rule(cls, value): #default rule
        return value

    @rule.register(AbstractFunction)
    @classmethod
    def rule_for_functions(cls, abstractfunction: AbstractFunction):
        abstractfunction.execute()
        return cls

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