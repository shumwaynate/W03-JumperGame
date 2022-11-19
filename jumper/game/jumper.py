
class Jumper:
    """The person falling down with a chute when they start off. 
    
    The responsibility of Jumper is to create a jumper, destroys each level of chute when called, 
    and when called returns if there is no more chute.
    
    Attributes:
        _jumper (List[String]): The actual jumper with chute and spikes.
    """

    
    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._jumper = [  
            "          " , 
            "   ___    ", 
            "  /___\   ", 
            "  \   /   ",
            "   \ /    ", 
            "    O     ",
            "   /|\    ",
            "   / \    ",
            "          ",
            " ^^^^^^^^ " ]

    def Jumper(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._jumper = [  
            "          " , 
            "   ___    ", 
            "  /___\   ", 
            "  \   /   ",
            "   \ /    ", 
            "    O     ",
            "   /|\    ",
            "   / \    ",
            "          ",
            " ^^^^^^^^ " ]
        
        
        
    def get_jumper(self):
        """Gets and prints the jumper.

        Args:
            self (Jumper): An instance of Jumper.
        
        """
        for i in range(len(self._jumper)):
            print(self._jumper[i])


    def doDestroyChute(self):
        """When called this method will destroy one layer of parachute.

        Args:
            self (Jumper): An instance of Jumper.
            
        """

        for i in range(len(self._jumper) - 1):
            self._jumper[i] = self._jumper[i+1]

        
    def ifDead(self):
        """Detects if there is any more parachute left, if not the return will be true
           thus ending the game.

        Args:
            self (Hider): An instance of Hider.

        Returns:
            boolean: False if there is still more parachute True if not, ends game
        """
        if self._jumper[0] == "    O     ": 
            print("You lost your parachute and Died!")
            return False
        else:
            return True
