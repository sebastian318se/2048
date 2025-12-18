import tkinter
from core import gamestate, runner

root = tkinter.Tk()

root.geometry("650x650")
root.title("2048")

root.configure(bg="bisque")

label = tkinter.Label(root, text = '2048', font = ('Clear Sans', 40, "bold"), pady=20, bg="bisque")
label.pack()

gameframe = tkinter.Frame(root, bg= "navajowhite3", padx = 5, pady = 5)
gameframe.place(x=325, y=300, anchor = "center")


last_key = None

def get_color(value):
    colors = {
        0: "navajowhite4",
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
    return colors.get(value, "bisque") # Get color if not 0


for row in gamestate.table:
    for cell in row:
        bgcolor = get_color(cell)

def ui_render():
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
                font = ('Clear Sans', 25 if cell_data < 1024 else 18,), 
                anchor = "center",
                bg = bgcolor)

            tile.grid(column = rowIndex, row = columnIndex, padx = 5, pady = 5)

def ui_controller():
    global last_key
    key = last_key
    last_key = None # Consumes input
    return key

# Separate functions to get direction and then return input
def on_key(event):
    global last_key
    if event.keysym in ("w","a","s","d"):
        last_key = event.keysym.lower()


# Calls on_key to save last_key
root.bind('<Key>', on_key)




runner.gameplay(ui_render, ui_controller, root)
root.mainloop()



# To break, exit button making condition true?



