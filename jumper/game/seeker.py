# TODO: Implement the Seeker class as follows...
class Seeker:
    # 1) Add the class declaration. Use the following class comment.

    def __init__(self):
        """The person looking for the Hider. 
    
        The responsibility of a Seeker is to keep track of its location and distance travelled.
    
        Attributes:
            location (int): The location of the Seeker (1-1000).
        """
        
        self._location = 0

    # 2) Create the class constructor. Use the following method comment.
    def Seeker(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._location = 0
       
    # 3) Create the get_location(self) method. Use the following method comment.
    def get_location(self):
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
        return self._location
        
    # 4) Create the move_location(self, location) method. Use the following method comment.
    def move_location(self, new_location):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self._location = new_location