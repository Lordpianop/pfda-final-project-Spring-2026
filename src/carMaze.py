import pygame

def main():
    titleSize = 40
    gridWidth = 15
    gridHeight = 15

    resolution = (titleSize * gridWidth, titleSize * gridHeight)
    screen = pygame.display.set_mode(resolution)