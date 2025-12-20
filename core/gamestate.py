import numpy

firstTurn = True
playerLost = False

table = numpy.array([
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ])

def get_score():
    score = 0
    for row in table:
        for cell in row:
            score += cell
    return score

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

def clear_table(table):
    y, x = 0, 0
    for y in range(len(table)):
         for x in range(len(table)):
              table[y][x] = 0