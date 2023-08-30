from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The mad King himself"""
    def __init__(self, first_name):
        super().__init__(first_name)
        baratheon_instance = Baratheon(first_name)
        self.family_name = baratheon_instance.first_name
        self.first_name = first_name

    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
