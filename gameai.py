from core import gamestate, movement, generation
from ai import posEvaluation

# TODO:
"""
Penalize player loss in eval(if no move is made on MAX node)
"""

def getEmptyTiles(table):
    emptyTiles = []
    for row, rowData in enumerate(table):
        for tile, tileData in enumerate(rowData):
            if tile == 0:
                emptyTiles.append([row, tile])
    return emptyTiles

class Node:
    def __init__(self, table, depth, nodeType, moveDirection, children, probability):
        self.table = table
        self.depth = depth
        self.nodeType = nodeType
        self.moveDirection = moveDirection
        self.children = children
        self.probability = probability

    def expand(self):
        if self.depth == 0:
            return
        
        # Execute every move available
        if self.nodeType == "MAX":
            for direction in ("w","a","s","d"):
                newTable = self.table.copy()
                # Check if movements are available
                if movement.move(direction, newTable):
                    # Create a child for each move executed
                    child = Node(
                        table = newTable,
                        depth = self.depth - 1,
                        nodeType = "CHANCE",
                        moveDirection = direction,
                        children = [],
                        probability = 1.0
                    )
                    self.children.append(child)
                    child.expand()

        # Run all possible tile spawns
        if self.nodeType == "CHANCE":
            emptyTiles = getEmptyTiles(self.table)
            for (x, y) in emptyTiles:
                for value, probEval in [(2, 0.9), (4, 0.1)]:
                    newTable = self.table.copy()
                    newTable[x][y] = value
                    # Create new child for each spawn executed
                    child = Node(
                        table = newTable,
                        depth = self.depth - 1,
                        nodeType = "MAX",
                        moveDirection = "a",
                        children = [],
                        # Store 0.9 and 0.1 as multipliers for node evaluation
                        probability = probEval
                    )
                    self.children.append(child)
                    child.expand()

    def evaluate(self):
        # Leaf node
        if self.depth == 0 or not self.children:
            score = posEvaluation.posEval(self.table)
            return score
        
        # Evaluate nodes individually going up the tree after leas are done
        # MAX node
        if self.nodeType == "MAX":
            return max(child.evaluate() for child in self.children)

        # CHANCE node
        if self.nodeType == "CHANCE":
            # Calculate evaluation of nodes wheighed by probability
            return sum(child.evaluate() * child.probability for child in self.children)