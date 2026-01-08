from math import log2

def posEval(table):
    evalScore = 0
    # Assign desired corner to bottom left
    desiredPos = [3, 0]
    biggestTilePos = [0, 0]
    biggestTile = -float('inf')

    weightScore = []
    weightEval = 0

    emptyTiles = False
    # Multiplicator for weight eval on each tile
    weighedTable = [
        [1.4, 1.2, 1.1, 1],
        [1.8, 1.4, 1.2, 1.1],
        [1.16, 1.8, 1.4, 1.2],
        [1.32, 1.16, 1.8, 1.4]
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

                # Decrease incrementally bigger fractions from eval score for big diffs
                for threshold, divisor in [(6, 2), (4, 6), (2, 8)]:
                    if threshold >= horizLogFoldChange:
                        evalScore -= (evalScore / divisor)

                # Repeat check vertically
                if table[row][tile] and table[row + 1][tile]:
                        # Use log2 formula to define how many merges away a tile is from its neighbor
                        vertLogFoldChange = abs(log2(table[row][tile]) - (log2(table[row + 1][tile])))
              
                for threshold, divisor in [(6, 2), (4, 6), (2, 8)]:
                    if threshold >= vertLogFoldChange:
                        evalScore -= (evalScore / divisor)

            except IndexError:
                pass

            # Weight evaluation for tiles closer to corner
            weightScore.append(table[row][tile] * weighedTable[row][tile])

            for value in weightScore:
                weightEval += value
            evalScore += weightEval

            # Award empty tiles
            if tileData == 0:
                evalScore += 1.05
                emptyTiles = True
            
            # Penalize no empty tiles (too close to a loss)
            if emptyTiles == False:
                evalScore -= 0.90

            # Award if biggest tile is in bottom left corner
            # TODO address equal values as biggest
            elif tileData >= biggestTile:
                biggestTile = tileData
                biggestTilePos = [row, tile]

    if biggestTilePos == desiredPos:
        evalScore += (evalScore * 1.32)

    return evalScore