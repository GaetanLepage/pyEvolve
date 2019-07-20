#!/bin/env python3

from grid import Grid
import time

"""
Game engine.
Contains the different data structures required.
Computes the future state of the sstructure.
"""
class Engine:
    def __init__(self, grid_size):
        """
        Constructor of an engine
        """
        self.current_grid = Grid(grid_size)
        self.next_grid = Grid(grid_size)
        
        # Instance of a class managing the display and the interaction
        self.ui = None
    
    def start(self):
        # TODO

        while True:
            self.step()
            time.sleep(20)

    def step(self):
        """
        Computes the next step of the system
        """
        for (cell, next_cell) in zip(self.current_grid.cells(), self.next_grid.cells()):
            assert cell.xpos == next_cell.xpos
            assert cell.ypos == next_cell.ypos

            alive_neighbors = cell.count_alive_neighbors()
            if alive_neighbors < 2 or alive_neighbors > 3:
                next_cell.die()
            if alive_neighbors == 3:
                next_cell.live()

        self.current_grid = self.next_grid
