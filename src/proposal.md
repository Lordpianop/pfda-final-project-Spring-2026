# Title
Car Maze Craze

## Repository
<https://github.com/Lordpianop/pfda-final-project-Spring-2026/tree/main>

## Description
This is a quick car-maze game, inspired by the NAMCO game "New Rally X", where you collect checkpoints to fill your draining gas meter. The game ends when the gas meter runs out. This project is relevant to media and digital arts because it is a simple replication of an existing video game.

## Features
- Player control
	- This will handle the movement of the player on the horizontal/vertical axis, and can only change directions once it reaches the next grid position. Player moves forward unless a wall tile is in the way. Movement will be similar to "New Rally X"
- Gas Tank
	- As time goes on, the gas tank meter gradually goes down. This acts as a time limit for the player. The gas tank can only be refilled when the player reaches a checkpoint. As more checkpoints are reached, the gas meter goes down quicker until it reaches zero. Once the gas meter reaches zero, the game ends.
- Checkpoints
	- Checkpoints spawn at random places in the maze and refill the gas tank when collected. Once a checkpoint is collected, it disappears, and a new one spawns at another random point in the maze.
- Maze
	- The maze will be the size of the game window (like a pacman maze), and will have walls that the player object collides with. The player will be able to move on ground tiles and be stopped at wall tiles.
- High Score system
	- High score system will save the amount of checkpoints reached in a csv file, and it'll update whenever the game ends and a new highest score is achieved.
- Game Over
	- Some kind of sequence where all systems stop, a giant "game over" text will appear, then the game closes. Score can also be displayed during game over.

## Challenges
- Smooth movement of an object that can be controlled with simple 'WASD' controls.
- Confining the player movement to the grid formation and implementing wall collisions.
- Making a meter that decreases, as well as making that rate faster after every checkpoint.
- Potentially implementing sound. I can research pygame sound systems.

## Outcomes
Ideal Outcome:
- Ideal outcome would be, along with base features implemented, extra art added on top of it all.
- Car sprite that points to the direction of movement
- Checkpoints look like yellow flags
- Maze will have a level of detail similar to "New Rally X" (stretch goal)
- Basic sound for movement, turns, checkpoint reach, and/or game over
- Level music (another stretch goal)

Minimal Viable Outcome:
- Minimal outcome would be to have a controllable moving object that can collect checkpoint objects, and if you don't collect the checkpoint objects fast enough, then the game ends.
- Score system should still be implemented, at least as a print statement in the terminal when the game ends.

## Milestones

- Week 1
  1. Grid player control implemented
  2. Simple maze set up (just as big as the screen)
  3. Checkpoint object disappears when touched by player object

- Week 2
  1. Gas meter with a game over function
  2. Checkpoint system implemented
  3. High score system

- Week 3 (Final)
  1. Car Sprite, points toward the direction of movement
  2. Maze Art
  3. Sound implementation