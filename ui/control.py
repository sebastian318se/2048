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

def player_mode_button(root, on_press):
    global player_button
    player_button = tkinter.Button(
        root,
        command = on_press,
        text = "Player Mode",
        font = ("Arial", 25, "bold"),
        bg = "navajowhite4",
        fg = "bisque",
        width = 10, height = 1
    )

    return player_button.place(x = 185, y = 300, anchor = "center")

def ai_mode_button(root, on_press):
    global ai_button
    ai_button = tkinter.Button(
        root,
        command = on_press,
        text = "AI Mode",
        font = ("Arial", 25, "bold"),
        bg = "navajowhite4",
        fg = "bisque",
        width = 10, height = 1
    )

    return ai_button.place(x = 415, y = 300, anchor = "center")

def deleter():
    global ai_button
    global player_button
    ai_button.destroy()
    player_button.destroy()
