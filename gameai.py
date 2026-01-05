from core import gamestate, movement, generation
from ai import posEvaluation


def maxNode():
    global searchTable
    searchTable = gamestate.table.copy()
    highestEval = 0
    highestDirection = ""

    # Calculate eval for each direction
    for direction in ("w","a","s","d"):
        if movement.move(direction, searchTable):
            currentEval, emptyTiles = posEvaluation.posEval(searchTable)
            print(direction, currentEval)

            if currentEval > highestEval:
                highestEval = currentEval
                highestDirection = direction

            chanceNode(emptyTiles)
            # Unmove
            searchTable = gamestate.table.copy()

    print("Best", highestDirection, highestEval)

def chanceNode(emptyTiles):
    # Make new generator function to generare a full node (all possibilities) for each direction moved
    # Eval recursively, with range budget

    # !! This is getting the values of the table after a move w/o considering generation after
    global searchTable
    print("Empty tiles:", emptyTiles)