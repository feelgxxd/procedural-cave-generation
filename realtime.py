import pygame
from grid import Grid
from rules import TwoPhaseCaveRule
from simulation import Simulation

BG_COLOR       = (26, 15, 11)
WALL_COLOR     = (110, 63, 42)
FLOOR_COLOR    = (35, 40, 50)
PREVIEW_COLOR  = (255, 255, 255)

WIDTH, HEIGHT = 120, 80
CELL_SIZE = 8
FPS = 30
EDIT_RADIUS = 2

SMOOTH_SPEED = 0.15

pygame.init()
screen = pygame.display.set_mode(
    (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
)
clock = pygame.time.Clock()

grid = Grid(WIDTH, HEIGHT, fill_probability=0.45, seed=42)
rule = TwoPhaseCaveRule(survival_min=3, birth_min=4)
sim = Simulation(grid, rule)

running = True
paused = False

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_r:
                grid = Grid(WIDTH, HEIGHT, 0.45)
                sim = Simulation(grid, rule)
                current_step = 0
            if event.key == pygame.K_LEFT:
                rule.survival_min = max(0, rule.survival_min - 1)
            if event.key == pygame.K_RIGHT:
                rule.survival_min += 1

            if event.key == pygame.K_DOWN:
                rule.birth_min = max(0, rule.birth_min - 1)
            if event.key == pygame.K_UP:
                rule.birth_min += 1

            if event.key == pygame.K_EQUALS:
                FPS = min(60, FPS + 1)
            if event.key == pygame.K_MINUS:
                FPS = max(1, FPS - 1)

    mouse_buttons = pygame.mouse.get_pressed()

    if paused:
        if mouse_buttons[0]:
            mx, my = pygame.mouse.get_pos()
            gx = mx // CELL_SIZE
            gy = my // CELL_SIZE
            grid.carve_circle(gx, gy, EDIT_RADIUS)

    if not paused:
        sim.step()

    screen.fill(BG_COLOR)

    for y in range(grid.height):
        for x in range(grid.width):
            base_rect = pygame.Rect(
                x * CELL_SIZE,
                y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, FLOOR_COLOR, base_rect)

    for y in range(grid.height):
        for x in range(grid.width):
            target = grid.cells[y][x]  # 0 veya 1
            grid.visual[y][x] += (target - grid.visual[y][x]) * SMOOTH_SPEED

    for y in range(grid.height):
        for x in range(grid.width):
            v = grid.visual[y][x]

            if v < 0.01:
                continue

            size = int(CELL_SIZE * v)
            offset = (CELL_SIZE - size) // 2

            rect = pygame.Rect(
                x * CELL_SIZE + offset,
                y * CELL_SIZE + offset,
                size,
                size
            )

            pygame.draw.rect(screen, WALL_COLOR, rect)

    mx, my = pygame.mouse.get_pos()
    gx = mx // CELL_SIZE
    gy = my // CELL_SIZE

    if paused:
        preview_rect = pygame.Rect(
            (gx - EDIT_RADIUS) * CELL_SIZE,
            (gy - EDIT_RADIUS) * CELL_SIZE,
            (EDIT_RADIUS * 2 + 1) * CELL_SIZE,
            (EDIT_RADIUS * 2 + 1) * CELL_SIZE
        )
        pygame.draw.rect(screen, (100, 150, 255), preview_rect, 1)

    pygame.display.flip()

pygame.quit()