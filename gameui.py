from core import gamestate, runner
from ui import headers, control, getgameframe
from ai import posEvaluation
import tkinter
import gameai

root = tkinter.Tk()

root.geometry("600x700")
root.title("2048")

root.configure(bg="bisque")

def new_game():
    global deleted
    deleted = False

    # if last game was a loss, generate 1. Else, generate 2 (using firstTurn)
    if runner.game_loop_id is not None:
        root.after_cancel(runner.game_loop_id)
        runner.game_loop_id = None

    if headers.loseLabel is not None:
        headers.del_lose_screen()
        deleted = True

    gamestate.clear_table(gamestate.table)

    if gamestate.playerLost:
        # Generate w/o making first turn false
        gamestate.firstTurnAfterLoss = True
        gamestate.playerLost = False # Re-enable movement
    else:
        gamestate.firstTurn = True
        gamestate.playerLost = False # Re-enable movement

    ui_render()
    get_mode()

def exit_game():
    root.destroy()

mode = None

def ai_mode():
    global mode
    mode = "AI"
    control.deleter()
    get_mode()

def player_mode():
    global mode
    mode = "PLAYER"
    control.deleter()
    get_mode()

headers.game_label(root)

gameframe = tkinter.Frame(root, bg= "navajowhite4", padx = 5, pady = 5)
gameframe.place(x = 300, y = 325, anchor = "center")

last_key = None
deleted = False 

def ui_render():
    global deleted
    posEvaluation.posEval(gamestate.table)
    
    control.new_game_button(root, new_game)
    control.exit_game_button(root, exit_game)

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

def ai_controller():
    global deleted
    ai_key = None

    rootNode = gameai.Node(
        table = gamestate.table.copy(),
        depth = 8,
        nodeType = "MAX",
        moveDirection = "",
        children = [],
        probability = 1.0
    )

    rootNode.expand()

    bestDirection = None
    maxEval = -float('inf')

    for child in rootNode.children:
        evalScore = child.evaluate()

        if evalScore > maxEval:
            maxEval = evalScore
            bestDirection = child.moveDirection


    # Use flag whenever lose screen is deleted
    if bestDirection is not None:
        ai_key = bestDirection
        deleted = False
        return ai_key
    
    elif deleted == False:
        gamestate.playerLost = True
        ui_render()
    

# Separate functions to get direction and then return input
def on_key(event):
    global last_key
    if event.keysym.lower() in ("w","a","s","d"):
        last_key = event.keysym.lower()


def get_mode():

    global mode
        
    if mode == None:
        control.player_mode_button(root, player_mode)
        control.ai_mode_button(root, ai_mode)

    if mode == "AI":
        runner.game_loop_id = runner.gameplay(ui_render, ai_controller, root)
    if mode == "PLAYER":
        # Calls on_key to save last_key
        runner.game_loop_id = runner.gameplay(ui_render, ui_controller, root)
        root.bind('<Key>', on_key)

get_mode()
root.mainloop()