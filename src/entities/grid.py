from entities.cell import Cell


class Grid:
    def __init__(self, size: int):
        self.size = size
        self.grid = [[] * size] * size
        for i in range(size):
            for j in range(size):
                self.grid[i][j] = Cell(i, j)

    @classmethod
    def from_grid(cls, other_grid):
        grid = cls(other_grid.size)
        for (cell, other_cell) in zip(grid.cells(), other_grid.cells()):
            assert cell.xpos == other_cell.xpos
            assert cell.ypos == other_cell.ypos
            cell.state = other_cell.state
        return grid

    def count_alive_neighbors(self, cell: Cell):
        count = 0
        for neighbor in self.neighbors(cell):
            count += neighbor.state
        return count

    def neighbors(self, cell: Cell):
        i, j = cell.ipos, cell.jpos
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if 0 < i + y < self.size and 0 < j + x < self.size:
                    yield self.grid[i + y][j + x]

    def cells(self):
        for line in self.grid:
            for cell in line:
                yield cell
