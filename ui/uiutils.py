import tkinter
from gameui import root, get_color, gameframe
from core import gamestate

def ui_render():
    scorelabel = tkinter.Label(root, text = ("Score:", gamestate.get_score()), bg = "bisque", fg = "navajowhite4", font = ('Arial', 25))
    scorelabel.place(x = 300, y = 100, anchor = "center")

    for widget in gameframe.winfo_children():
        widget.destroy()

    # Getting all positions on gamestate.table 
    for columnIndex, columndata in enumerate(gamestate.table):
        for rowIndex, cell_data in enumerate(columndata):
            
            bgcolor = get_color(cell_data)

            tile = tkinter.Label(
                gameframe,
                text = "" if cell_data == 0 else cell_data,
                width = 4, height = 2,
                font = ('Arial', 25 if cell_data < 1024 else 18,), 
                anchor = "center",
                bg = bgcolor)

            tile.grid(column = rowIndex, row = columnIndex, padx = 5, pady = 5)