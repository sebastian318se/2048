import tkinter

def get_color(value):
    colors = {
        0: "navajowhite3",
        2: "bisque",
        4: "peachpuff",
        8: "sandybrown",
        16: "tan1",
        32: "tan2",
        64: "tomato",
        128: "khaki1",
        256: "khaki2",
        512: "khaki3",
        1024: "gold2",
        2048: "goldenrod1"
    }
    return colors.get(value, "bisque")


def draw_grid(frame, table):
    for columnIndex, columndata in enumerate(table):
        for rowIndex, cell_data in enumerate(columndata):
            
            bgcolor = get_color(cell_data)

            tile = tkinter.Label(
                frame,
                text = "" if cell_data == 0 else cell_data,
                width = 4, height = 2,
                font = ('Arial', 25 if cell_data < 1024 else 18,), 
                anchor = "center",
                bg = bgcolor)

            tile.grid(column = rowIndex, row = columnIndex, padx = 5, pady = 5)
