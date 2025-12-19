import tkinter
from core import gamestate, runner, generation

root = tkinter.Tk()

root.geometry("750x700")
root.title("2048")

root.configure(bg="bisque")

def exit_game():
    root.destroy()

def new_game():
    gamestate.clear_table()
    gamestate.playerLost = False
    generation.isCoordAv(2)
    ui_render()
    runner.gameplay(ui_render, ui_controller, root)
    

label = tkinter.Label(root, text = "2048", font = ("Arial", 40, "bold"), pady=20, bg="bisque", fg="navajowhite4")
label.place(x = 300, y = 50, anchor = "center")

newGame = tkinter.Button(root, command = new_game, text = "New Game", font = ("Arial", 25, "bold"), bg = "navajowhite4", fg = "bisque", width = 9, height = 1)
newGame.place(x = 200, y = 575, anchor = "center")

exitButton = tkinter.Button(root, command = exit_game, text = "Exit Game", font = ("Arial", 25, "bold"), bg = "navajowhite4", fg = "bisque", width = 9, height = 1)
exitButton.place(x = 400, y = 575, anchor = "center")

gameframe = tkinter.Frame(root, bg= "navajowhite4", padx = 5, pady = 5)
gameframe.place(x = 300, y = 325, anchor = "center")

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

for row in gamestate.table:
    for cell in row:
        bgcolor = get_color(cell)


last_key = None

def ui_render():
    scorelabel = tkinter.Label(root, text = ("Score:", gamestate.get_score()), width = 10, height = 1, bg = "bisque", fg = "navajowhite4", font = ('Arial', 25))
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

def ui_controller():
    global last_key
    key = last_key
    last_key = None # Consume input
    return key

# Separate functions to get direction and then return input
def on_key(event):
    global last_key
    if event.keysym.lower() in ("w","a","s","d"):
        last_key = event.keysym.lower()

# Calls on_key to save last_key
root.bind('<Key>', on_key)
runner.gameplay(ui_render, ui_controller, root)
root.mainloop()

"""
FINISH UI:

Losing screen
Exit button -> done
New game button -> otw
modularize
Save data from previous games
Percentage screen
"""