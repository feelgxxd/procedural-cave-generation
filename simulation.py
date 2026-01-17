# simulation.py
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

        for y in range(self.grid.height):
            for x in range(self.grid.width):
                old = self.grid.cells[y][x]
                new = new_cells[y][x]

                if old != new:
                    self.grid.reaction[y][x] = 1.0 if new == 1 else -1.0

                self.grid.cells[y][x] = new