from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Character.

        Parameters:
        first_name (str): The first name of the character.
        is_alive (bool, optional): The health state of the character.
        Default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Method to change the health state of the character.

        This method should be implemented by subclasses to change the
        health state of the character from alive to dead.
        """
        pass


class Stark(Character):
    """Class representing a Stark character."""
    def __init__(self, first_name, is_alive=True):
        """
        Stark character has been created
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
            In halls of red, a joyous feast did bloom,
            Yet shadows hid the doom, impending gloom.
            Alliances shattered, trust cruelly unfurled,
            A wedding turned to massacre, a treacherous world.

            Robb's honor, Catelyn's plea, all in vain,
            The Rains of Castamere sang a deadly refrain.
            Beneath the banners, life's river ran cold,
            The Red Wedding's tale, a tragic story told.
            Change the health state of the Stark character to False.

            This method overrides the abstract method from the base class and
            updates the is_alive attribute to False.
        """
        self.is_alive = False
