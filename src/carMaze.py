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

    maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,1,1,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,1,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,1,0,1,0,0,0,1],
    [1,0,1,0,1,0,0,0,0,0,1,0,1,0,1],
    [1,0,1,0,0,0,1,1,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]


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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and game_over:
                    if event.key == pygame.K_r:
                        main()
                        return
                    elif event.key == pygame.K_q:
                        running = False
        
        if not game_over:

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
                        if maze[new_row][new_col] == 0:
                            player.grid_position = (new_col, new_row)

                        move_timer = 0
                
                        if player.grid_position == checkpoint.grid_position:
                            checkpoint_pos = get_random_floor_position(maze)
                            checkpoint.grid_position = checkpoint_pos
                            gas = max_gas
                            score += 1
                            print("Score:", score)

        

                    

        
        screen.fill((20, 20, 20))
         
        gridColor = pygame.Color(40, 40, 40)

        for row in range(gridHeight):
            for col in range(gridWidth):
                x = col * tileSize
                y = row * tileSize

                square = pygame.Rect(x, y, tileSize, tileSize)

                if maze[row][col] == 1:
                    pygame.draw.rect(screen, (0, 90, 155), square)
                else:
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

        if game_over:
            gameOver_fontsize = pygame.font.SysFont(None, 72)
            restart_fontsize = pygame.font.SysFont(None, 40)

            gameOver_text = gameOver_fontsize.render("GAME OVER", True, (255, 50, 50))
            restart_text = restart_fontsize.render("Press R to Restart", True, (255, 255, 255))
            quit_text = restart_fontsize.render("Press Q to Quit", True, (200, 200, 200))

            gameOver_position = gameOver_text.get_rect(center=(resolution[0] // 2, 220))
            restart_position = restart_text.get_rect(center=(resolution[0] // 2, 300))
            quit_position = quit_text.get_rect(center=(resolution[0] // 2, 340))

            screen.blit(gameOver_text, gameOver_position)
            screen.blit(restart_text, restart_position)
            screen.blit(quit_text, quit_position)


        pygame.display.flip()

        dt = clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()