import random

class Puzzle:
    """The Puzzle to solve during the game. Consists of a secret word that needs to be uncovered by guessing letters one at a time.
    
    The responsibility of the Puzzle is to control and display if it has been solved or not.

    Attributes:
        _word (string): the secret word the player needs to guess.
        _hidden_word (string): the secret word shown with its characters hidden.
        _is_solved (bool): whether the Puzzle has been solved or not.
    """

    def __init__(self):
        """Constructs a new Puzzle.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        self._word = self._get_word()
        self._hidden_word = self._hide_word(self._word)
        self._is_solved = False

    def _get_word(self):
        """Selects a random word from a predetermined list.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        words = ['funny', 'lucky', 'avenue', 'banjo', 'buffalo', 'cycle', 'fluffy', 'exodus', 'gossip', 'injury', 'jazz', 'joking', 'juicy', 'luxury', 'nowadays', 'pixel', 'pajama', 'puppy', 'quiz', 'quorum', 'rhythm', 'staff', 'stretch', 'subway', 'unknown', 'unworthy', 'wave', 'wizard', 'youthful', 'zigzag', 'zombie', 'food', 'plant', 'apple']

        return random.choice(words)

    def _hide_word(self, word):
        """Replaces the characters of a word by underscores.
        
        Args:
            self (Puzzle): an instance of Puzzle.
            word (string): the word to be hidden.
        """
        hidden_word = ''
        for _ in range(len(word)):
            hidden_word += '_ '

        return hidden_word

    def show_word(self):
        """Shows the secret word.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return self._word

    def display_word(self):
        """Displays the secret word with its characters hidden.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return self._hidden_word

    def check_guess(self, guess):
        """Checks if the player's guess is correct.
        
        Args:
            self (Puzzle): an instance of Puzzle.
            guess (string): a single letter representing the player's guess
        """
        return guess in self._word

    def reveal_letter(self, letter):
        """Reveals a hidden character if it is contained in the secret word.
        
        Args:
            self (Puzzle): an instance of Puzzle.
            letter (string): a single character to be shown.
        """
        if letter in self._word:
            letters = list(self._word)
            indexes = [i for i,l in enumerate(letters) if l == letter]
            split_hidden = list(self._hidden_word)
            for index in indexes:
                split_hidden[index*2] = letter

            self._hidden_word = ''.join(split_hidden)
            
    def update_solved(self):
        """Updates the state of the Puzzle if it has been solved.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        self._is_solved = '_' not in self._hidden_word

    def check_solved(self):
        """Tells whether or not the Puzzle has been solved.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return self._is_solved

    