# ==========================================
# Whack-a-Mole - Part 1
# New in this part: game window + 9 holes
# ==========================================

import pygame

pygame.init()

# ----- Window -----
WIDTH = 600
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-a-Mole")
clock = pygame.time.Clock()

# ----- Colors (Red, Green, Blue) -----
GRASS = (110, 190, 90)
DIRT = (120, 80, 45)
HOLE = (50, 30, 15)
WHITE = (255, 255, 255)

# ----- Font -----
font = pygame.font.SysFont("arial", 40, bold=True)

# ----- Hole positions -----
# 3 rows x 3 columns = 9 holes
holes = []
for row in range(3):
    for col in range(3):
        x = 120 + col * 180
        y = 230 + row * 150
        holes.append((x, y))


# Draw one hole at position (x, y)
def draw_hole(x, y):
    pygame.draw.ellipse(screen, DIRT, (x - 65, y - 22, 130, 44))
    pygame.draw.ellipse(screen, HOLE, (x - 55, y - 16, 110, 32))


# ----- Game loop -----
running = True
while running:

    # 1. Check events (keyboard, mouse, close button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Draw everything
    screen.fill(GRASS)

    title = font.render("Whack-a-Mole", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

    for x, y in holes:
        draw_hole(x, y)

    # 3. Show the new frame
    pygame.display.flip()
    clock.tick(60)  # 60 frames per second

pygame.quit()
