#!/bin/env python3

"""
Class representing a cell.
Each cell is linked to its grid
It can be either dead or alive
"""
class Cell:

    def __init__(self, ipos, jpos, grid, state=0):
        """
        Constructor for class cell
        """
        # Cell position
        self.ipos = ipos
        self.jpos = jpos

        # Cell state
        self.state = False

        # Grid to which the cell belongs
        self.grid = grid

    def live(self):
        """
        Make the cell "live" / "born" (set its state to True)
        """
        if not self.state:
            self.grid.alive_cell_counter += 1
            self.state = True

    def die(self):
        """
        Make the cell "die" (set its state to False)
        """
        if self.state:
            self.grid.alive_cell_counter -= 1
            self.state = False


    def count_alive_neighbors(self):
        """
        **return:**
            * The number of alive neighbors of the cell.
        """
        n_alive_neighbors = 0
        for neighbor in self.grid.neighbors(self):
            if neighbor.state:
                n_alive_neighbors += 1

        return n_alive_neighbors
