from Choosables.Menus.AbstractMenu import AbstractMenu


class Submenu1(AbstractMenu):

    @classmethod
    def __init__(cls):
        from Choosables.Menus.Implementations.MainMenu import MainMenu
        from Choosables.Menus.Implementations.Submenu2 import Submenu2
        super().__init__([MainMenu, Submenu2])

    @classmethod
    def to_string(cls):
        return "Submenu1"
