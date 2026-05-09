# PROJECT TITLE
Project Speed Maze Craze

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <https://github.com/Lordpianop/pfda-final-project-Spring-2026/tree/main>

## Description
[explain what your project is, what do the different files in my repository contain or do, any design considerations, future areas of improvements]
My project is a game inspired by the NAMCO classic "New Rally-X". In this game, the player moves along a grid with WASD [hold or tap] to collect yellow checkpoints before the time meter runs out. The game starts out simple, but progressively becomes more difficult as the timer drains quicker with each checkpoint collected. Get the highest score you can in this race against the clock!

This project was an extension of the knowledge I accumulated from weekly class notes. I created the player in a grid-based system using the class system, making the player move using particle systems similar to the screen saving lab. I also expanded on the visuals by adding simple UI and a smooth decreasing timer bar, which was accomplished by updating the width of a green bar with the pivot point set to one side. I stored the data of the maze into a long 01 data list, making future maze ideas easily customizeable. This maze data system also makes it easy to randomize where the checkpoint square will be, since it has to only pick a random floor (0) tile to be the next checkpoint. I added onto the pygame quit function by adding a "game over" state that prompts the player to restart or quit. This project only contains a main project file and a csv file to store the high score data. 

While I didn't get to everything I wanted (art, music, sound), I'm happy with the result of this project. It's in a playable state that can challenge any player. Future improvements for this project might include smooth and continuous movement of the car instead of snappy hold-key movements. I may also want to add in sound and music to make the game more engaging, as well as expand on the visuals of the player and environment. If I wanted to go even further, I could make a larger map for the player to drive through and add more threats/obstacles. There's a lot that could be expanded on with this project. 