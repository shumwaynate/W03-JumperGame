from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's puzzle.
        is_playing (boolean): Whether or not to keep playing.
        umper (Jumper): The game's jumper.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        self._guess = ""
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            
        self._do_outputs()
        

    def _get_inputs(self):
        """Gets the main puzzle, the jumper and question printed for the user to guess a letter

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.getPuzzleHidden()
        self._jumper.get_jumper()
        self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        
        
    def _do_updates(self):
        """Checks user inputs, communicates between objects to destroy a layer of the parachute,
        resets parachute attributes, and tests if the jumper is dead or if the player won.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.spellCheck(self._guess)
        destroyChute = False
        destroyChute = self._puzzle.getIfDestroyChute()
        if destroyChute == True:
            self._jumper.doDestroyChute()
        self._puzzle.doResetChute()
        self._is_playing = self._jumper.ifDead()

        self._is_playing = self._puzzle.testWin()

        
    def _do_outputs(self):
        """Prints out that the game is now over

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text("The game is over!")
        