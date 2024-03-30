

def GameOver(finishers:list, board:list):
        # Vraca:
    # None ako je kraj partije bez pobednika
    #  1   ako je pobedio X
    # -1   ako je pobedio O
    #  0   ako niko nije pobedio (jos se igra)
    none = False
    for line in finishers:
        game_over = []
        for square in line:
            check = board[square[1]][square[0]]
            if check!=None:
                game_over.append(check)
            else:
                none = True
                game_over.clear()
                break
        if game_over and all(v==True for v in game_over):
            print(line)
            return 1
        elif game_over and all(v==False for v in game_over):
            print(line)
            return -1
    else:
        return None if none==False else 0 
