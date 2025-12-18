import numpy
import core.gamestate as gamestate

def move(direction):
        
        grid = gamestate.table
        rotated =  0
        reverse = False

        if direction == "w":
            # rot90(ARRAY, number of times flipped counter clockwise)
            grid = numpy.rot90(gamestate.table)
            rotated += 1
            
        if direction == "d":
            # Reverse table on its own axis
            grid = [row[::-1] for row in grid]
            reverse = True

        if direction == "s":
            grid = numpy.rot90(gamestate.table, k=-1)
            rotated -= 1

        newlist = []

        for row in grid:
            tempList = []

            for item in row:
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

        # Fill each row with zeroes
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

        gamestate.table = grid