import csv
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

class Checkpoint():
    def __init__(self, grid_position=(0, 0), size=40):
        self.grid_position = grid_position
        self.size = size
        self.color = pygame.Color(255, 200, 0)
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
    
    
def get_random_floor_position(maze):
    while True:
        row = random.randrange(len(maze))
        col = random.randrange(len(maze[0]))

        if maze[row][col] == 0:
            return (col, row)

def load_high_score():
    try:
        with open("high_score.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                return int(row[0])
    except:
        return 0
    
def save_high_score(score):
    with open("high_score.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([score])

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

    checkpoint_pos = get_random_floor_position(maze)
    checkpoint = Checkpoint(grid_position=checkpoint_pos, size=tileSize)

    dt = 0

    gas = 100
    max_gas = 100
    drain_rate = 0.02

    score = 0
    font = pygame.font.SysFont(None, 36)

    high_score = load_high_score()

    move_timer = 0
    move_delay = 120

    game_over = False

    while running:
        gas -= drain_rate * dt
        if gas <= 0 and not game_over:
            game_over = True
            print("Game Over")

            if score > high_score:
                high_score = score
                save_high_score(score)
                print("New High Score!")

            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False

        move_timer += dt
        if move_timer >= move_delay:

            keys = pygame.key.get_pressed()

            col, row = player.grid_position
            new_col, new_row = col, row

            if keys[pygame.K_w]:
                new_row -= 1
            elif keys[pygame.K_s]:
                new_row += 1
            elif keys[pygame.K_a]:
                new_col -= 1
            elif keys[pygame.K_d]:
                new_col += 1

            if (new_col, new_row) != (col, row):
                if 0 <= new_col < gridWidth and 0 <= new_row < gridHeight:
                    player.grid_position = (new_col, new_row)

                    move_timer = 0
                
                    if player.grid_position == checkpoint.grid_position:
                        checkpoint_pos = get_random_floor_position(maze)
                        checkpoint.grid_position = checkpoint_pos
                        gas = max_gas
                        score += 1
                        print("Score:", score)

        

                    

        
        screen.fill((0, 0, 0))
         
        gridColor = pygame.Color(50, 50, 50)

        for row in range(gridHeight):
            for col in range(gridWidth):
                x = col * tileSize
                y = row * tileSize

                square = pygame.Rect(x, y, tileSize, tileSize)
                pygame.draw.rect(screen, gridColor, square, 1)
        checkpoint.draw(screen)
        player.draw(screen)

        bar_width = 200
        bar_height = 20
        bar_x = 10
        bar_y = 10

        pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, 
                                                   bar_width, bar_height))
        
        gas_width = int((gas / max_gas) * bar_width)
        pygame.draw.rect(screen, (0, 200, 0), (bar_x, bar_y, gas_width, bar_height))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 40))

        high_score_text = font.render(f"High Score: {high_score}", True, (200, 200, 200))
        screen.blit(high_score_text, (430, 10))


        pygame.display.flip()

        dt = clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()