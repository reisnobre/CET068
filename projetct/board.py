"""."""
import numpy as np


def create_grid():
    """."""
    grid = np.empty((10, 10), dtype=Cell)
    for line in range(9):
        for col in range(9):
            grid[line, col] = Cell((line, col))

    return grid


class Cell:
    """."""

    def __init__(self, coordinates, value=1):
        """."""
        self.coordinates = coordinates
        self.value = value


class Board:
    """."""

    def __init__(self):
        """."""
        self.grids = []
        self.grids.append(create_grid())

    def last_grid(self):
        """."""
        return self.grids[len(self.grids) - 1]

    def set_cell(self, coordinates, value):
        """."""
        new_grid = create_grid()

        self.copy(new_grid)

        new_grid[coordinates[0], coordinates[1]].value = value

        self.grids.append(new_grid)

    def copy(self, new_grid):
        """."""
        last_grid = self.last_grid()

        for line in range(9):
            for col in range(9):
                new_grid[line, col].value = last_grid[line, col].value

        # self.grids.append(grid)

    def print(self, grid=None):
        """."""
        if grid is None:
            grid = self.last_grid()
        for line in range(9):
            for col in range(9):
                print(grid[line, col].value, end=' ')
            print('\n', end='')

    def print_full(self):
        """."""
        for grid in self.grids:
            print("============================")
            self.print(grid)

    def check_bounds(self, node):
        line = node.coordinates[0]
        col = node.coordinates[1]
        if line <= 9 and line >= 0 and col <= 9 and col >= 0:
            return True
