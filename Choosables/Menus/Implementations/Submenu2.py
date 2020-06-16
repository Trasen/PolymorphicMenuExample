from Choosables.Menus.AbstractMenu import AbstractMenu


class Submenu2(AbstractMenu):

    @classmethod
    def __init__(cls):
        from Choosables.Menus.Implementations.Submenu1 import Submenu1
        super().__init__([Submenu1])

    @classmethod
    def to_string(cls):
        return "Submenu2"
