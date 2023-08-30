from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name):
        super().__init__(first_name)
        self.first_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"Vector: ({self.first_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """Why rob a bank when you can marry a Lannister and inherit the vault?"""
    def __init__(self, first_name):
        super().__init__(first_name)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"Vector: ({self.first_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
