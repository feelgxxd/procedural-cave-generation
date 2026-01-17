# visualize.py
def print_ascii(grid):
    for row in grid.cells:
        print("".join("#" if cell else "." for cell in row))