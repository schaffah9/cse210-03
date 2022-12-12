class Jumper:
    """The Jumper represents the player's opportunities to guess the correct answer to the puzzle.
    
    The responsibility of the Jumper is to control and display the remaining guesses available to the player to try to win the game.

    Attributes:
        _body (list[string]): the Jumper's body.
        _parachute (list[string]): the Jumper's parachute representing the amount of guesses remaining.
        _is_alive (bool): whether the player has any remaining guesses or not.
    """
    
    def __init__(self):
        """Constructs a new Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self._body = ["   O  ", "  /|\ ", "  / \ "]
        self._parachute = ["  ___ ", " /___\\", " \   /", "  \ / "]
        self._is_alive = True

    def _has_parachute(self):
        """Tells if the Jumper still has a parachute, representing if the player still has any guesses remaining.
        
        Args:
            self (Jumper): an instance of Jumper.

        Returns:
            bool: True if Jumper has a piece of parachute attached, false if otherwise.
        """
        return len(self._parachute) > 0

    def display(self):
        """Displays the Jumper and its parachute to the player.
        
        Args:
            self (Jumper): an instance of Jumper.
        Returns:
            string: multi-line string showing parachute attached to the body of the Jumper.
        """
        jumper = self._parachute + self._body
        
        separator = '\n'
        return separator.join(jumper)

    def detach_piece(self):
        """Removes a part of the parachute, indicating that the guess was incorrect.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self._parachute.pop(0)

    def update_life(self):
        """Updates the state of the Jumper if the whole parachute has been removed, indicating that the player has lost the game.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        if not self._has_parachute():
            self._is_alive = False
            self._body[0] = "   X  "

    def check_life(self):
        """Tells if the Jumper is still alive, which indicates if the player can continue the game.
        
        Args:
            self (Jumper): an instance of Jumper.
        Returns:
            bool: True if the player has any guesses remaining, false if otherwise.
        """
        return self._is_alive
