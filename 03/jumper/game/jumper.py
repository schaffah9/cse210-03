class Jumper:
    
    def __init__(self):
        self._body = ["   O  ", "  /|\ ", "  / \ "]
        self._parachute = ["  ___ ", " /___\\", " \   /", "  \ / "]
        self._is_alive = True

    def _has_parachute(self):
        return len(self._parachute) > 0

    def display(self):
        jumper = self._parachute + self._body
        
        separator = '\n'
        return separator.join(jumper)

    def detach_piece(self):
        self._parachute.pop(0)

    def update_life(self):
        if not self._has_parachute():
            self._is_alive = False
            self._body[0] = "   X  "

    def check_life(self):
        return self._is_alive
