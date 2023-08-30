from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""
    
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Character.
        
        Parameters:
        first_name (str): The first name of the character.
        is_alive (bool, optional): The health state of the character. Default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive
        
    @abstractmethod
    def die(self):
        """
        Method to change the health state of the character.
        
        This method should be implemented by subclasses to change the health state of
        the character from alive to dead.
        """
        pass


class Stark(Character):
    """Class representing a Stark character."""
    
    def die(self):
        """
        Change the health state of the Stark character to False.
        
        This method overrides the abstract method from the base class and updates
        the is_alive attribute to False.
        """
        self.is_alive = False

