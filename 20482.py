# Import tabulate for cleaner terminal interface // random for coordinate generating
# Import numpy for transposition and reversing list (simplify movement)
from tabulate import tabulate
import random
import numpy

# Set up terminal interface 
table = numpy.array([
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ])



firstTurn = True
playerLost = False

while playerLost == False:
    # Change row X, column Y to 2
    def genTwo(coord1, coord2):
        ranNumb = [2,2,2,2,4]
        num = random.choice(ranNumb)
        table[coord1][coord2] = num

    # Criar nested list com valores das coordenadas disponiveis, chamar table[coord1][coord2] = 2
    avCoordsList = []

    # Add available coordinate values to nested list; call ranCoord()
    def isCoordAv():
        rowCount = 0
        columnCount = 0
        for i in table:
            for j in i:
                if j == 0:
                    avCoordsList.append([rowCount, columnCount])
                    columnCount += 1
                elif j != 0:
                    columnCount += 1

                if columnCount >= 4:
                    columnCount = 0
            rowCount += 1
        ranCoord()

    # Select random coordinate from avCoordsList and call genTwo with the chosen coordinate
    def ranCoord():


        global playerLost
        if not avCoordsList:
            print("\033[91mNO POSITIONS AVAILABLE! PLAYER LOST!\033[0m")
            playerLost = True

            
        else:
            # Get random coordinate from avCoordsList
            rdmCoord = random.choice(avCoordsList)
            # Call genTwo function with chosen coordinate
                # Very important: using * as an unpacking operator to get both coordinates from list pos
            genTwo(*rdmCoord)
            avCoordsList.clear()

    def color_tile(value):
        colors = {
            2: "\033[97m",    # White
            4: "\033[96m",    # Cyan
            8: "\033[94m",    # Blue
            16: "\033[92m",   # Green
            32: "\033[33m",   # Yellow
            64: "\033[91m",   # Red
            128: "\033[95m",  # Pink
            256: "\033[90m",  # Gray
            512: "\033[31m",  # Maroon
            1024: "\033[35m", # Purple
            2048: "\033[94m", # Blue
        }
        reset = "\033[0m"
        color = colors.get(value, "\033[97m")  # Default to white
        return f"{color}{value if value != 0 else '.'}{reset}"

    def move(direction):
        global table
        
        grid = table
        rotated =  0
        reverse = False

        if direction == "w":
            # rot90(ARRAY, number of times flipped COUNTER CLOCKWISE)
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
                    i += 1 # Make sure not to fully add the lines (2,2,4 should NOT = 8, should be (4,4))

                else:
                    i += 1

        # Fill each row with zeroes to get it back to make it complete length again
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

        table = grid

    if firstTurn:
        isCoordAv()
        coloredStartTable = [[color_tile(cell) for cell in row] for row in table]
        print(tabulate(coloredStartTable, tablefmt = "double_grid"))
        firstTurn = False

    dirInput = input("\033[95mDirection (W, A, S, D):\033[0m")
    dirInput.lower()
    if dirInput in ("w","a","s","d"):
        move(dirInput)
        isCoordAv()

        score = 0
        for s in table:
            for t in s:
                score += t

        
        coloredTable = [[color_tile(cell) for cell in row] for row in table]
        print(tabulate(coloredTable, tablefmt="double_grid"))


        print("Score:", score)
        
    elif dirInput == "break":
        playerLost = True
    else:
        print("Invalid Input. Use WASD / wasd")
