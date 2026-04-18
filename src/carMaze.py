import pygame

def main():
    titleSize = 40
    gridWidth = 15
    gridHeight = 15

    resolution = (titleSize * gridWidth, titleSize * gridHeight)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False