from Choosables.Functions.AbstractFunction import AbstractFunction


class SayHi(AbstractFunction):

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def execute(cls):
        print("Hi there!")

    @classmethod
    def to_string(cls):
        return "Python says hi :)"
