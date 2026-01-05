import numpy
from core import gamestate

def move(direction, table = None):
        
        # Assign gamestate.table if this is being run from the game and not evaluator
        if table is None:
            table = gamestate.table
        # Check if moved and rerturn true or false
        moved = False

        grid = table
        rotated =  0
        reverse = False

        if direction == "w":
            # rot90(ARRAY, number of times flipped counter clockwise)
            grid = numpy.rot90(table)
            rotated += 1
            
        if direction == "d":
            # Reverse table on its own axis
            grid = [row[::-1] for row in grid]
            reverse = True

        if direction == "s":
            grid = numpy.rot90(table, k=-1)
            rotated -= 1

        newlist = []

        for row in grid:
            tempList = []

            for item in row:
                # New list per row ignoring all zeroes
                if item != 0:
                    tempList.append(int(item))

            newlist.append(tempList)

        for row in newlist:

            i = 0

            # While i index is less than the amount of indexes (run for all positions)
            while i < len(row) - 1:
                # If current value is the same as the next, add them
                if row[i] == row[i + 1]:
                    row[i] *= 2
                    # Delete added row
                    del row[i + 1]
                    # Move to the next index
                    i += 1

                else:
                    i += 1

        # Reset table
        for row in newlist:
            while len(row) < 4:
                row.append(0)
                i += 1

        grid = newlist

        if rotated > 0:
            grid = numpy.rot90(grid, k=-1)
        elif rotated < 0:
            grid = numpy.rot90(grid)
        if reverse:
            grid = [row[::-1] for row in grid]

        # Check if movement happened
        if not numpy.array_equal(table, grid):
            for r in range(4):
                for c in range(4):
                    # Update table to be the same as grid
                    table[r][c] = grid [r][c]
            moved = True
        return moved
