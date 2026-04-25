import pygame
import random


class Player():
    def __init__(self, grid_position=(0, 0), size=40):
        self.grid_position = grid_position
        self.size = size
        self.color = pygame.Color(0, 200, 0)
        self.surface = self.update_surface()
    
    def update_surface(self):
        surface = pygame.Surface((self.size, self.size))
        surface.fill(self.color)
        return surface
    
    def draw(self, screen):
        col, row = self.grid_position
        x = col * self.size
        y = row * self.size
        screen.blit(self.surface, (x, y))

def main():
    pygame.init()
    pygame.display.set_caption("Car Maze Craze")
    tileSize = 40
    gridWidth = 15
    gridHeight = 15

    resolution = (tileSize * gridWidth, tileSize * gridHeight)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()
    player = Player(grid_position=(7, 7), size=tileSize)
    running = True

    maze = []
    for row in range(gridHeight):
        maze_row = []
        for col in range(gridWidth):
            maze_row.append(0)
        maze.append(maze_row)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                col, row = player.grid_position
                new_col, new_row = col, row

                if event.key == pygame.K_w:
                    new_row -= 1
                elif event.key == pygame.K_s:
                    new_row += 1
                elif event.key == pygame.K_a:
                    new_col -= 1
                elif event.key == pygame.K_d:
                    new_col += 1

                if 0 <= new_col < gridWidth and 0 <= new_row < gridHeight:
                    player.grid_position = (new_col, new_row)
        
        screen.fill((0, 0, 0))
         
        gridColor = pygame.Color(50, 50, 50)

        for row in range(gridHeight):
            for col in range(gridWidth):
                x = col * tileSize
                y = row * tileSize

                square = pygame.Rect(x, y, tileSize, tileSize)
                pygame.draw.rect(screen, gridColor, square, 1)
        player.draw(screen)


        pygame.display.flip()

        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()