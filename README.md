# Tic Tac Toe — Python

A command-line Tic Tac Toe project built in Python, featuring two game modes: a classic two-player game and an unbeatable AI opponent powered by the **Minimax algorithm**.

---

## Features

- **Two-Player Mode** — Play locally against a friend, taking turns in the terminal.
- **AI Mode** — Face off against an AI that uses the Minimax algorithm to play perfectly. It cannot be beaten — your best outcome is a draw.
- **Win Detection** — Automatically checks all rows, columns, and diagonals after every move.
- **Draw Detection** — Recognizes when the board is full with no winner.

---

## How It Works

### Two-Player Mode (`two_player_tictactoe.py`)

The board is represented as three lists (`top`, `middle`, `bottom`). Players are prompted to enter a row (1–3) and column (1–3) on each turn. Input is validated to prevent overwriting filled cells. The game ends when a winning combination is detected or all cells are filled.

### AI Mode (`ai_tictactoe.py`)

The board is a flat list of 9 cells. The AI plays as `X` and the human plays as `O`. Before each AI move, the **Minimax algorithm** recursively simulates every possible future game state, scoring outcomes as:

| Outcome | Score |
|---|---|
| AI (`X`) wins | `+1` |
| Human (`O`) wins | `-1` |
| Draw | `0` |

The AI always picks the move with the highest score, making it theoretically unbeatable.

---

## Getting Started

### Prerequisites

- Python 3.x

### Running the Two-Player Game

```bash
python two_player_tictactoe.py
```

Enter a **row** (1–3) and **column** (1–3) when prompted.

### Running the AI Game

```bash
python ai_tictactoe.py
```

The AI moves first. Enter a position from **0–8** when it's your turn, mapped as follows:

```
0 | 1 | 2
3 | 4 | 5
6 | 7 | 8
```

---

## Project Structure

```
.
├── two_player_tictactoe.py   # Local two-player game
├── ai_tictactoe.py           # Single-player game vs. Minimax AI
└── README.md
```

---

## Concepts Demonstrated

- Recursive algorithms (Minimax)
- Game state representation and manipulation
- Input validation and game loop design
- Win/draw condition checking

---
