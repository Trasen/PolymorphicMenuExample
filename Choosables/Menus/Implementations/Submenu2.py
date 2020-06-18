from Choosables.Functions.Implementations.SayHi import SayHi
from Choosables.Menus.AbstractMenu import AbstractMenu


class Submenu2(AbstractMenu):

    @classmethod
    def __init__(cls):
        super().__init__([SayHi])

    @classmethod
    def to_string(cls):
        return "Submenu2"
