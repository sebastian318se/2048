import core.gamestate as gamestate
import random 

avCoordsList = []

def genTwo(coord1, coord2):
    ranNumb = [2,2,2,2,4]
    num = random.choice(ranNumb)
    gamestate.table[coord1][coord2] = num

# Add available coordinate values to nested list; call ranCoord()
def isCoordAv(count = 1):
    for i in range(count):
        rowCount = 0
        columnCount = 0
        for i in gamestate.table:
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

# Select random coordinate from avCoordsList and call genTwo
def ranCoord():
    try:
        if not avCoordsList and gamestate.noMerges(gamestate.table) == False:
            gamestate.playerLost = True

        else:
            # Get random coordinate from avCoordsList
            rdmCoord = random.choice(avCoordsList)
            # Call genTwo function with chosen coordinate
            genTwo(*rdmCoord)
            avCoordsList.clear()
    except IndexError:
        # Don't do anything if no available tiles and player inputs invalid move.
        pass

        
    