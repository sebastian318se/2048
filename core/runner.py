from core import gamestate, generation, movement

score = 0

game_loop_id = None
# Using parameter as function to render gamestate.table diff methods
def gameplay(renderer, controller, root=None):
    global game_loop_id
    global score
    if not gamestate.playerLost:
        if gamestate.firstTurn:
            generation.isCoordAv(True, 2)

            # Call to update ui/ terminal interface
            renderer()
            
            gamestate.firstTurn = False

        # Get input from current runner
        dirInput = controller()

        if dirInput in ("w","a","s","d"):
            hasMoved = movement.move(dirInput)
            
            generation.isCoordAv(hasMoved)
            renderer()

        elif dirInput == "break":
            return

        if root:
            # After 100ms, call gameplay(renderer, controller, root) as game_loop_id n(if player loses, cancel scheduled afters)
            game_loop_id = root.after(100, gameplay, renderer, controller, root)

        else:
            # Call gameplay(renderer, controller)
            if not gamestate.playerLost:
                gameplay(renderer, controller)
