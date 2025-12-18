from core import gamestate, generation, movement

score = 0
# Using parameter as function to render gamestate.table diff nmethods
def gameplay(renderer, controller, root=None):
    global score
    if gamestate.playerLost:
        return
    if gamestate.firstTurn:
        generation.isCoordAv(2)

        # Call to update ui/ terminal interface
        renderer()
        
        gamestate.firstTurn = False

    # Get input from current used runner
    dirInput = controller()

    if dirInput in ("w","a","s","d"):
        movement.move(dirInput)
        generation.isCoordAv()

        score = 0
        for s in gamestate.table:
            for t in s:
                score += t

        renderer()

    elif dirInput == "break":
        return

    if root:
        # After 100ms, call gameplay(renderer, controller, root)
        root.after(100, gameplay, renderer, controller, root)

    else:
        # Call gameplay(renderer, controller)
        if not gamestate.playerLost:
            gameplay(renderer, controller)
