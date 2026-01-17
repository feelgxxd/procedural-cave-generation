# cave/grid.py
import random

class Grid:
    def __init__(self, width, height, fill_probability=0.45, seed=None):
        self.width = width
        self.height = height
        self.fill_probability = fill_probability

        if seed is not None:
            random.seed(seed)

        self.cells = self._random_fill()

        self.visual = [
            [float(self.cells[y][x]) for x in range(width)]
            for y in range(height)
        ]

        self.reaction = [
            [0.0 for _ in range(width)]
            for _ in range(height)
        ]

    def _random_fill(self):
        return [
            [
                1 if random.random() < self.fill_probability else 0
                for _ in range(self.width)
            ]
            for _ in range(self.height)
        ]

    def is_wall(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return True
        return self.cells[y][x] == 1

    def count_wall_neighbors(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                if self.is_wall(x + dx, y + dy):
                    count += 1
        return count
    
    def carve_circle(self, cx, cy, radius):
        for y in range(cy - radius, cy + radius + 1):
            for x in range(cx - radius, cx + radius + 1):
                if (x - cx)**2 + (y - cy)**2 <= radius**2:
                    if 0 <= x < self.width and 0 <= y < self.height:
                        self.cells[y][x] = 0