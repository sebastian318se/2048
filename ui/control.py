import tkinter

def exit_game_button(root, on_press):

    exitButton = tkinter.Button(
        root,
        command = on_press,
        text = "Exit Game",
        font = ("Arial", 25, "bold"),
        bg = "navajowhite4",
        fg = "bisque",
        width = 9, height = 1)
    
    return exitButton.place(x = 400, y = 575, anchor = "center")

def new_game_button(root, on_press):

    newGame = tkinter.Button(
        root,
        command = on_press,
        text = "New Game",
        font = ("Arial", 25, "bold"),
        bg = "navajowhite4",
        fg = "bisque",
        width = 9, height = 1)
    
    return newGame.place(x = 200, y = 575, anchor = "center")
