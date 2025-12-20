import tkinter
# Make into display?

def game_label(root):
    gameLabel = tkinter.Label(
        root,
        text = "2048",
        font = ("Arial", 40, "bold"),
        pady=20,
        bg="bisque", fg="navajowhite4")
    
    return gameLabel.place(x = 300, y = 50, anchor = "center")

def update_score(root, newscore):
    scorelabel = tkinter.Label(
        root,
        text = ("Score:", newscore),
        font = ('Arial', 25),
        width = 10, height = 1, 
        bg = "bisque", 
        fg = "navajowhite4", 
       )
    return scorelabel.place(x = 300, y = 100, anchor = "center")

def lose_screen(root):
    global loseLabel
    loseLabel = tkinter.Label(
        root,
        text = "Game Over!",
        font = ("Arial", 35, "bold"),
        bg = "navajowhite4"
    )

    return loseLabel.place(x = 300, y = 325, anchor = "center")

def del_lose_screen():
    global loseLabel
    loseLabel.destroy()