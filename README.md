# Arcade Hub

## Description

Arcade Hub is a personal Python and Pygame project focused on recreating several classic arcade-style games inside a single application.

The project is being built incrementally with an emphasis on clean code, reusable game components, frame-rate-independent movement, and maintainable game architecture. Pong is the first game being developed and currently supports a complete local two-player match loop.

## Technologies
Python 3.13
Pygame 2.6.1
Current Game: Pong

Pong is currently playable with two local players.

## Features
Two-player local controls
Frame-rate-independent paddle and ball movement
Paddle movement boundaries
Ball collision with paddles
Ball collision with top and bottom walls
Collision handling for wall and paddle edge cases
Player scoring
Ball reset after each point
Configurable winning score
Game-over state
Winner display
Match restart
Resolution-relative positioning
Controls
Player	Move Up	Move Down
Left Player	W	S
Right Player	Up Arrow	Down Arrow

After a match ends, press Space to restart.

## Running the Project
Clone the repository.
Create and activate a Python virtual environment.
Install the required dependencies:
pip install -r requirements.txt
Run the application:
python main.py

## Project Structure
arcade-hub/
├── main.py
├── requirements.txt
├── README.md
└── games/
    └── pong/
        ├── pong.py
        ├── paddle.py
        └── ball.py

main.py manages the shared application window and game loop, while each game is responsible for its own state, update logic, and rendering.

## Planned Development

Pong will continue to receive gameplay and presentation improvements before development moves to additional games.

Planned games currently include:

Pong
Snake
Flappy-style game
Tetris-style game

Longer-term improvements may include an Arcade Hub game-selection menu, configurable settings and controls, sound effects, additional game modes, and retro CRT-inspired visual effects.

Status

Arcade Hub is actively under development. Pong is the first playable game, with additional gameplay polish and arcade games planned.