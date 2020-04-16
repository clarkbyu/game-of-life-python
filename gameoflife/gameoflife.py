# gameoflife.py
""" 
Clark Brown
Game of Life
"""

import numpy as np

class Game:
    def __init__(self, start_state, rules, size):
        self.start_state = start_state
        self.rules = rules
        self.size = size

    def run_game(self, iters):
        """ Runs the game of life iterating iters times or until a the
        system stabilizes. 

        Parameters:
            iters (int): The maximum number of times to iterate

        Returns:
            (list(ndarray)): the grid at each stage of the game
            (bool): If the system stabilized during the iterations
        """
        state = self.start_state
        prev_state = None
        game_progress = []
        stable = False

        for _ in range(iters):
            prev_state = state.copy()
            game_progress.append(prev_state.grid)
            state = state.transition(self.rules, self.size)
            
            # System has stabilized
            if (state == prev_state):
                stable = True
                break

        return game_progress, stable

