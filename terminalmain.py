from core import gamestate, runner
from tabulate import tabulate


def render():
    coloredTable = [[gamestate.color_tile(cell) for cell in row] for row in gamestate.table]
    print(tabulate(coloredTable, tablefmt="double_grid"))

# Start gameplay, running render() whenever table changes 
runner.gameplay(render)
