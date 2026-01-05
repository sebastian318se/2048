from core import gamestate, movement
from ai import posEvaluation


def chooseDirection():
    searchTable = gamestate.table.copy()
    highestEval = 0
    highestDirection = ""

    # Calculate eval for each direction
    for direction in ("w","a","s","d"):
        if movement.move(direction, searchTable):
            currentEval = posEvaluation.tileEval(searchTable)
            print(direction, currentEval)

            if currentEval > highestEval:
                highestEval = currentEval
                highestDirection = direction
            # Unmove
            searchTable = gamestate.table.copy()

    print("Best", highestDirection, highestEval) 


"""
Clone table
Move -> evaluate max node / chance node
Evaluate best case scenario of all lookups for each direction
Undo changes (or just clone searchtable back into og table)
Choose direction

After this is running, incorporate chance node eval
"""