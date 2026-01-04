# 2048
This is was a project for my _Intro to Computer Science_ class at FGCU.  
It is based off the popular game [2048](https://play2048.co/) and designed to run entirely in the terminal using Python.

# Features
- 2048 game clone  
- tkinter UI
- Expectimax AI using heuristics

# Game Logic Overview
Movements are handled by:  
Rotating the grid with numpy.rot90 to move up/ down  
Reversing rows to move right/ down  
Compacting tiles left → merging → filling with zeros

After each move:  
A check scans for open coordinates.
A new tile (2 or 4) spawns.
Score is recalculated as the sum of all tile values.

# Used tools
- Python 3
- [NumPy](https://numpy.org/)  
- [Tabulate](https://pypi.org/project/tabulate/)  

# License
MIT.
