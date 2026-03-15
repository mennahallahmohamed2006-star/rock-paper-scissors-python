# 🎮 Rock Paper Scissors Game (Python)

This is a functional, terminal-based **Rock, Paper, Scissors** game. I built it to practice Python fundamentals like functions, loops, and conditional logic.

## 🛠️ How it Works
The game follows a structured approach using separate functions:
* `get_user_choice()`: Validates that the player enters a valid move.
* `get_computer_choice()`: Uses the `random` library to pick the computer's move.
* `winner()`: Contains the game logic to decide who won the round.
* `main()`: The engine that runs the game, tracks scores, and handles the "play again" loop.

## ✨ Features
- **Input Validation:** The game won't crash if you type something wrong; it asks you to try again.
- **Score Tracking:** Keeps a running tally of your wins vs. the computer's wins.
- **Replayability:** You can play as many rounds as you want until you choose to exit.

## 🚀 How to Run
1. Clone this repository or download the `RockPaperScissors.py` file.
2. Run it using Python:
   ```bash
   python RockPaperScissors.py
