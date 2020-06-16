from Choosables.Functions.Implementations.Exit import Exit
from Choosables.Functions.Implementations.SayHi import SayHi
from Choosables.Menus.AbstractMenu import AbstractMenu


class MainMenu(AbstractMenu):

    @classmethod
    def __init__(cls):
        from Choosables.Menus.Implementations.Submenu2 import Submenu2
        from Choosables.Menus.Implementations.Submenu1 import Submenu1
        super().__init__([Submenu1, Submenu2, Exit, SayHi])

    @classmethod
    def to_string(cls):
        return "Huvudmenyn"
