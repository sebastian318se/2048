import tkinter
from core import gamestate, runner, generation
from ui import headers, control, getgameframe

root = tkinter.Tk()

root.geometry("600x700")
root.title("2048")

root.configure(bg="bisque")

def new_game():
    # if last game was a loss, generate 1. Else, generate 2 (using firstTurn)
    if runner.game_loop_id is not None:
        root.after_cancel(runner.game_loop_id)
        runner.game_loop_id = None

    gamestate.clear_table(gamestate.table)

    try:
        headers.del_lose_screen()
    except NameError:
        pass
    finally:
        if gamestate.playerLost:
            # Generate w/o making first turn false
            gamestate.firstTurnAfterLoss = True
            gamestate.playerLost = False # Re-enable movement
            runner.gameplay(ui_render, ui_controller, root)
        else:
            gamestate.firstTurn = True
            gamestate.playerLost = False # Re-enable movement
            runner.gameplay(ui_render, ui_controller, root)
            
def exit_game():
    root.destroy()

headers.game_label(root)
control.new_game_button(root, new_game)
control.exit_game_button(root, exit_game)

gameframe = tkinter.Frame(root, bg= "navajowhite4", padx = 5, pady = 5)
gameframe.place(x = 300, y = 325, anchor = "center")

last_key = None

def ui_render():
    
    if gamestate.playerLost:
        headers.lose_screen(root)

    headers.update_score(root, gamestate.get_score())

    for widget in gameframe.winfo_children():
        widget.destroy()

    getgameframe.draw_grid(gameframe, gamestate.table)

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
runner.game_loop_id = runner.gameplay(ui_render, ui_controller, root)
root.mainloop()

# Final updates to make:
# Check if no av coords AND no av merges for player lost - done
# Optimization w/ bug fix - don't call gameplay multiple times
