# simulation.py
from grid import Grid

class Simulation:
    def __init__(self, grid, rule):
        self.grid = grid
        self.rule = rule

    def step(self):
        new_cells = [
            [0 for _ in range(self.grid.width)]
            for _ in range(self.grid.height)
        ]

        for y in range(self.grid.height):
            for x in range(self.grid.width):
                neighbors = self.grid.count_wall_neighbors(x, y)
                new_cells[y][x] = self.rule.apply(
                    self.grid.cells[y][x],
                    neighbors
                )

        self.grid.cells = new_cells