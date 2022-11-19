import random

class Puzzle:
    """Gets puzzle word and makes a hidden word, check inputs if in puzzle word

    
    The responsibility of Puzzle is to create a Puzzle, destroys each level of chute when called, 
    and when called returns if there is no more chute.
    
    Attributes:
        _puzzleword (String): the word chosen at random chosen from a list for the puzzle
        _puzzleHidden(List(String)): The puzzle word with letters replaced with '_'
        _wordLength(int): The length of the selected puzzle word to simplify code
        destroyChute(boolean): Used to detect if the provided input matches the puzzle word
    """

    def __init__(self):
        """The Puzzle constructor, preaparing a game of hangman style puzzle 
    
        The responsibility of a Seeker is to keep track of its location and distance travelled.
    
        Attributes:
            location (int): The location of the Seeker (1-1000).
        """
        
        self._puzzleWord = random.choice(["apple", "orange", "banana", "pineapple", "kiwi"])
        self._puzzleHidden = []
        self._wordLength = len(self._puzzleWord)
        for i in range(self._wordLength):
            self._puzzleHidden.append("_")
        self.destroyChute = False

    def Puzzle(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        
        
    def spellCheck(self, guess):
        """Tests if the guess is in the word, replacing letters if it does, setting the parachute
        to be destroyed in future.
        
        Args:
            self (Puzzle): An instance of Puzzle.
            guess(string): User's input guess letter
        """
        
        self._testCorrect = 0

        for i in range(self._wordLength):
            if guess == self._puzzleWord[i]:
                self._puzzleHidden[i] = guess
                self._testCorrect += 1
            else:
                pass
        
        self.setDestroyChute()

        if (self._testCorrect >= 1 ):
            self.destroyChute = False
        

            

    def getIfDestroyChute(self):
        """Gets and returns if the chute needs to be destroyed one layer.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            boolean(self._destroyChute): True if one layer of the chute needs to be destroyed.
        """
        return self.destroyChute

    def testWin(self):
        """Tests if the puzzle has been solved

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            boolean(self._destroyChute): False if the game has been won, ending game.
        """
        count = 0
        for i in range(self._wordLength):
            if self._puzzleHidden[i] == self._puzzleWord[i]:
                count +=1
        if count == self._wordLength:
            print("You win!!!")
            print(self._puzzleWord+"!")
            return False
        else:
            return True

    def doResetChute(self):
        """Resets Encapsulated boolean for the destroyedChute back to False

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            boolean(self._destroyChute): True if one layer of the chute needs to be destroyed.
        """
        self.destroyChute = False
    
    def getPuzzleHidden(self):
        """Prints out the secret coded puzzle

        Args:
            self (Puzzle): An instance of Puzzle.
        
        """
        print (*self._puzzleHidden)

    def setDestroyChute(self):
        """ Sets the destroyChute attribute to true

        Args:
            self(Puzzle): An instance of Puzzle
        """
        self.destroyChute = True

    
