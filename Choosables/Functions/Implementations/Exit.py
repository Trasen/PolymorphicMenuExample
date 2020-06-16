import sys

from Choosables.Functions.AbstractFunction import AbstractFunction


class Exit(AbstractFunction):

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def execute(cls):
        sys.exit()

    @classmethod
    def to_string(cls):
        return "Exit"
