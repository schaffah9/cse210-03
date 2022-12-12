import random

class Puzzle:

    def __init__(self):
        self._word = self._get_word()
        self._hidden_word = self._hide_word(self._word)
        self._is_solved = False

    def _get_word(self):
        words = ['funny', 'lucky', 'avenue', 'banjo', 'buffalo', 'cycle', 'fluffy', 'exodus', 'gossip', 'injury', 'jazz', 'joking', 'juicy', 'luxury', 'nowadays', 'pixel', 'pajama', 'puppy', 'quiz', 'quorum', 'rhythm', 'staff', 'stretch', 'subway', 'unknown', 'unworthy', 'wave', 'wizard', 'youthful', 'zigzag', 'zombie', 'food', 'plant', 'apple']

        return random.choice(words)

    def _hide_word(self, word):
        hidden_word = ''
        for _ in range(len(word)):
            hidden_word += '_ '

        return hidden_word

    def show_word(self):
        return self._word

    def display_word(self):
        return self._hidden_word

    def check_guess(self, guess):
        return guess in self._word

    def reveal_letter(self, letter):
        if letter in self._word:
            letters = list(self._word)
            indexes = [i for i,l in enumerate(letters) if l == letter]
            split_hidden = list(self._hidden_word)
            for index in indexes:
                split_hidden[index*2] = letter

            self._hidden_word = ''.join(split_hidden)
            
    def update_solved(self):
        self._is_solved = '_' not in self._hidden_word

    def check_solved(self):
        return self._is_solved

    