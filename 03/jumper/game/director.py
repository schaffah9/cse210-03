from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _jumper (Jumper): The game's jumper.
        _is_playing (boolean): Whether or not to keep playing.
        _puzzle (Puzzle): The game's puzzle.
        _terminal_service (TerminalService): For getting and displaying information on the terminal.
        _guess (string): player's guess to solve the puzzle.
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
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()

    def _get_inputs(self):
        """Asks the player to guess a letter.

        Args:
            self (Director): An instance of Director.
        """
        if self._is_playing:
            valid_guess = False
            while not valid_guess:
                prompt = 'Guess a letter [a-z]: '
                self._guess = self._terminal_service.read_text(prompt).lower()
                valid_guess = self._guess in 'abcdefghijklmnopqrstuvwxyz'
                if not valid_guess:
                    message = 'Guess not valid, please try again.'
                    self._terminal_service.write_text(message)
            print()
        
    def _do_updates(self):
        """Updates game state.

        Args:
            self (Director): An instance of Director.
        """
        if self._is_playing:
            if self._puzzle.check_guess(self._guess):
                self._puzzle.reveal_letter(self._guess)
            else:
                self._jumper.detach_piece()

            self._jumper.update_life()
            self._puzzle.update_solved()
        
    def _do_outputs(self):
        """Displays the Jumper, the Puzzle, and other messages to the player.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(self._puzzle.display_word())
        print()
        self._terminal_service.write_text(self._jumper.display())
        print()
        self._terminal_service.write_text('^^^^^^^')
        print()
        if self._puzzle.check_solved():
            self._is_playing = False
            win_message = 'Congratulations. You won the game!'
            self._terminal_service.write_text(win_message)
        if not self._jumper.check_life():
            self._is_playing = False
            loss_message = 'Game over. You lost the game!'
            self._terminal_service.write_text(loss_message)

        if not self._is_playing:
            self._get_inputs()
            final_message = f'The secret word was "{self._puzzle.show_word()}"'
            self._terminal_service.write_text(final_message)
        