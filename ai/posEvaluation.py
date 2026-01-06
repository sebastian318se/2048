from math import log2

def posEval(table):
    evalScore = 0
    # Assign desired corner to bottom left
    desiredPos = [3, 0]
    biggestTilePos = [0, 0]
    biggestTile = 0

    weightScore = []
    weightEval = 0

    # Multiplicator for weight eval on each tile
    weighedTable = [
        [4, 2, 1, 0],
        [8, 4, 2, 1],
        [16, 8, 4, 2],
        [32, 16, 8, 4]
    ]


    for row, rowData in enumerate(table):
        for tile, tileData in enumerate(rowData):

            try:
                horizLogFoldChange = 0
                vertLogFoldChange = 0

                # Penalize big changes between neighboring tiles
                if table[row][tile] and table[row][tile + 1]:
                    # Use log2 formula to define how many merges away a tile is from its neighbor
                    horizLogFoldChange = abs(log2(table[row][tile]) - (log2(table[row][tile + 1])))

                if horizLogFoldChange >= 6:
                    evalScore -= 2048
                elif horizLogFoldChange >= 3:
                    evalScore -= 256

                # Repeat check vertically
                if table[row][tile] and table[row + 1][tile]:
                        # Use log2 formula to define how many merges away a tile is from its neighbor
                        vertLogFoldChange = abs(log2(table[row][tile]) - (log2(table[row + 1][tile])))

                if vertLogFoldChange >= 6:
                    evalScore -= 2048
                elif vertLogFoldChange >= 3:
                    evalScore -= 256

            except IndexError:
                pass

            # Weight evaluation for tiles closer to corner
            weightScore.append(table[row][tile] * weighedTable[row][tile])

            for value in weightScore:
                weightEval += value
            evalScore += weightEval

            # Award empty tiles
            if tileData == 0:
                evalScore += 1024
            
            # Award if biggest tile is in bottom left corner
            # TODO address equal values as biggest
            elif tileData >= biggestTile: 
                biggestTile = tileData
                biggestTilePos = [row, tile]

    if biggestTilePos == desiredPos:
        evalScore *= 2

    return evalScore
        