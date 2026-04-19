import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Car Maze Craze")
    tileSize = 40
    gridWidth = 15
    gridHeight = 15

    resolution = (tileSize * gridWidth, tileSize * gridHeight)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))
         
        gridColor = pygame.Color(50, 50, 50)

        for row in range(gridHeight):
            for col in range(gridWidth):
                x = col * tileSize
                y = row * tileSize

                square = pygame.Rect(x, y, tileSize, tileSize)
                pygame.draw.rect(screen, gridColor, square, 1)


        pygame.display.flip()

        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()