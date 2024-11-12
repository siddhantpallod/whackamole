import pygame
import random

GRID_WIDTH = 20
GRID_HEIGHT = 16
SQUARE_SIZE = 32

def draw_grid(screen):
    for x in range(GRID_WIDTH + 1):
        pygame.draw.line(screen, "dark green", (x * SQUARE_SIZE, 0), (x * SQUARE_SIZE, 512))

    for y in range(GRID_WIDTH + 1):
        pygame.draw.line(screen, "dark green", (0, y * SQUARE_SIZE), (640, y * SQUARE_SIZE))

def move_mole(mole_rect):
    random_x = random.randrange(0, GRID_WIDTH) * SQUARE_SIZE
    random_y = random.randrange(0, GRID_HEIGHT) * SQUARE_SIZE
    mole_rect.topleft = (random_x, random_y)

def main():
    try:
        pygame.init()

        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-mole")
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect(topleft = (0, 0))

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        move_mole(mole_rect)

            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
