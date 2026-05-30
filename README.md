# IDA* for Romania Cities

A faculty project implementing the **IDA\* (Iterative Deepening A\*)** pathfinding algorithm to find the shortest route between major Romanian cities.

## What it does

Given a start and destination city, the algorithm finds the optimal path through a graph of ~40 Romanian cities connected by real road distances. A Euclidean heuristic is used to guide the search.

## Tech Stack

- Python 3
- Tkinter (GUI)
- JSON (heuristic table)

## Project Structure

```
├── IDAScript/
│   ├── script.py                  # Core IDA* implementation
│   └── heuristic_table_romania.json
└── GUI/
    └── gui.py                     # Tkinter interface
```

## How to Run

```bash
# Run the algorithm directly
python IDAScript/script.py

# Or launch the GUI
python GUI/gui.py
```

## Algorithm

IDA\* works like DFS with an iterative cost threshold — starts at `h(start, goal)` and increases the threshold until the goal is found. The heuristic is scaled Euclidean distance between cities based on pixel coordinates on a map image.

## Cities Covered

40+ Romanian cities including București, Cluj-Napoca, Timișoara, Iași, Constanța, Brașov, Sibiu, and more.
