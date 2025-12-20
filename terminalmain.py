from core import gamestate, runner
from tabulate import tabulate

def terminal_render():
    coloredTable = [[gamestate.color_tile(cell) for cell in row] for row in gamestate.table]
    print(tabulate(coloredTable, tablefmt="double_grid"))
    print("Score:", gamestate.get_score())

def terminal_controller():
    return input("\033[95mDirection (W, A, S, D):\033[0m").strip().lower()

# controller() = input handling; render() = retrieve + print table changes
runner.gameplay(terminal_render, terminal_controller)