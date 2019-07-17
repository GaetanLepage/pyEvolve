class Engine:
    def __init__(self, grid):
        self.current_grid = grid
        self.next_grid = grid

    def step(self):
        for (cell, next_cell) in zip(self.current_grid.cells(), self.next_grid.cells()):
            assert cell.xpos == next_cell.xpos
            assert cell.ypos == next_cell.ypos

            alive_neighbors = self.current_grid.count_alive_neighbors(cell)
            if alive_neighbors < 2 or alive_neighbors > 3:
                next_cell.die()
            if alive_neighbors == 3:
                next_cell.live()

        self.current_grid = self.next_grid
