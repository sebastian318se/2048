from math import log2

def posEval(table):
    evalScore = 0
    # Assign desired corner to bottom left
    desiredPos = [3, 3]
    biggestTilePos = [0, 0]
    biggestTile = -float('inf')

    weightScore = []
    weightEval = 0
    empties = 0

    emptyTiles = False
    # Multiplicator for weight eval on each tile
    weighedTable = [
        [1, 1.1, 1.2, 1.4],
        [1.1, 1.2, 1.4, 1.8],
        [1.2, 1.4, 1.8, 1.16],
        [1.4, 1.8, 1.16, 1.32]
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

                # Repeat check vertically
                if table[row][tile] and table[row + 1][tile]:
                        # Use log2 formula to define how many merges away a tile is from its neighbor
                        vertLogFoldChange = abs(log2(table[row][tile]) - (log2(table[row + 1][tile])))
              
                for threshold, divisor in [(6, 2), (4, 6), (2, 8)]:
                    if vertLogFoldChange >= threshold:
                        evalScore -= (evalScore / divisor)
                
                # Decrease incrementally bigger fractions from eval score for big diffs
                for threshold, divisor in [(6, 2), (4, 6), (2, 8)]:
                    if horizLogFoldChange >= threshold:
                        evalScore -= (evalScore / divisor)
            except IndexError:
                pass

            # Weight evaluation for tiles closer to corner
            weightEval += (table[row][tile] * weighedTable[row][tile])

            # Award empty tiles
            if tileData == 0:
                empties += 1

            # Increment based on amount of empty tiles
            evalScore += empties * 2.7

            # Penalize no empty tiles (too close to a loss)
            if empties == 0:
                evalScore -= 0.95

            # Award if biggest tile is in bottom left corner
            # TODO address equal values as biggest
            elif tileData >= biggestTile:
                biggestTile = tileData
                biggestTilePos = [row, tile]
    
    evalScore += weightEval
    evalScore += monotonicity(table) * 2

    if biggestTilePos == desiredPos:
        evalScore += biggestTile * 3
    return evalScore

def monotonicity(table):
    score = 0
    for row in table:
        for i in range(3):
            if row[i] >= row[i+1] and row[i] != 0:
                score += log2(row[i])

    for col in range(3):
        for i in range(3):
            if table[i][col] >= table[i][col + 1] and table[i][col] != 0:
                score += log2(table[i][col])
    return score