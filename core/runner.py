from core import gamestate, generation, movement

# Using parameter as function to render gamestate.table diff nmethods
def gameplay(renderer):
    while not gamestate.playerLost:
        if gamestate.firstTurn:
            generation.isCoordAv(2)

            # Print in terminal/ update ui
            renderer()
            
            gamestate.firstTurn = False

        dirInput = input("\033[95mDirection (W, A, S, D):\033[0m").strip().lower()

        if dirInput in ("w","a","s","d"):
            movement.move(dirInput)
            generation.isCoordAv()

            score = 0
            for s in gamestate.table:
                for t in s:
                    score += t

            renderer()

            print("Score:", score)
            
        elif dirInput == "break":
            break
        else:
            print("Invalid Input. Use WASD / wasd")