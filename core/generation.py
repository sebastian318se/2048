import core.gamestate as gamestate
import random 

avCoordsList = []

def genTwo(coord1, coord2, table):
    num = 2 if random.random() < 0.9 else 4 # 90% 2, 10% 4
    table[coord1][coord2] = num

# Add available coordinate values to nested list; call ranCoord()
def isCoordAv(moved, count = 1, table = None):
    if table is None:
        table = gamestate.table
    for i in range(count):
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
        ranCoord(moved, table)

# Select random coordinate from avCoordsList and call genTwo
def ranCoord(moved, table):
    try:
        if gamestate.firstTurn:
            rdmCoord = random.choice(avCoordsList)
            genTwo(*rdmCoord, table)

        # Isolated generation after loss to avoid tkinter root.after bug
        elif gamestate.firstTurnAfterLoss:
            for i in range(2):
                rdmCoord = random.choice(avCoordsList)
                genTwo(*rdmCoord, table)
            gamestate.firstTurnAfterLoss = False

        else:
            # Check if player hasn't lost
            if not avCoordsList and gamestate.noMerges(table) == False:
                gamestate.playerLost = True
            # Check if player has moved on last turn
            elif moved:
                # Get random coordinate from avCoordsList
                rdmCoord = random.choice(avCoordsList)
                # Call genTwo function with chosen coordinate
                genTwo(*rdmCoord, table)
                avCoordsList.clear()
    except IndexError:
        # Don't do anything if no available tiles and player inputs invalid move.
        pass

        
    