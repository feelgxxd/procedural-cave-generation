import pygame
from PIL import Image
from grid import Grid
from rules import TwoPhaseCaveRule
from simulation import Simulation

BG_COLOR       = (26, 15, 11)
WALL_COLOR     = (110, 63, 42)
FLOOR_COLOR    = (35, 40, 50)
PREVIEW_COLOR  = (255, 255, 255)
BIRTH_COLOR    = (165, 242, 165)
DEATH_COLOR    = (220, 120, 120)

WIDTH, HEIGHT = 120, 80
CELL_SIZE = 8
FPS = 30
EDIT_RADIUS = 2

SMOOTH_SPEED = 0.15

BRUSH_ALPHA = 80
BRUSH_COLOR = (200, 220, 255)

show_heatmap = False

pygame.init()

def heatmap_color(n):

    t = min(max(n / 8, 0), 1)

    r = int(255 * t)
    g = int(100 * (1 - t))
    b = int(255 * (1 - t))

    return (r, g, b)

def create_brush_surface(radius, cell_size):
    size = (radius * 2 + 1) * cell_size
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    
    center = size // 2
    pygame.draw.circle(
        surf,
        (*BRUSH_COLOR, BRUSH_ALPHA),
        (center, center),
        radius * cell_size
    )
    return surf

brush_surface = create_brush_surface(EDIT_RADIUS, CELL_SIZE)

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

            if event.key == pygame.K_h:
                show_heatmap = not show_heatmap

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
            target = grid.cells[y][x]
            grid.visual[y][x] += (target - grid.visual[y][x]) * SMOOTH_SPEED

            grid.reaction[y][x] *= 0.60
            if abs(grid.reaction[y][x]) < 0.05:
                grid.reaction[y][x] = 0

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

            if show_heatmap:
                n = grid.count_wall_neighbors(x, y)
                color = heatmap_color(n)
            else:
                r = grid.reaction[y][x]
                if r > 0:
                    color = BIRTH_COLOR
                elif r < 0:
                    color = DEATH_COLOR
                else:
                    color = WALL_COLOR

            pygame.draw.rect(screen, color, rect)

    mx, my = pygame.mouse.get_pos()
    gx = mx // CELL_SIZE
    gy = my // CELL_SIZE

    if paused:
        screen.blit(
            brush_surface,
            (
                (gx - EDIT_RADIUS) * CELL_SIZE,
                (gy - EDIT_RADIUS) * CELL_SIZE
            )
        )

    pygame.display.flip()

pygame.quit()