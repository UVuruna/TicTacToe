


    
def GameOver(finishers:list, board:list): # Faster - Sto je duza partija to se vise povecava razlika u brzini
        # Vraca:
    # None ako je kraj partije bez pobednika
    #  1   ako je pobedio X
    # -1   ako je pobedio O
    #  0   ako niko nije pobedio (jos se igra)
    none = False
    for line in finishers:
        game_over = None
        for square in line:
            check = board[square[1]][square[0]]
            if check!=None:
                if game_over is None:
                    game_over = board[square[1]][square[0]]
                elif check!=game_over:
                    break
            else:
                none = True
                break
        else:
            return -1 if game_over==False else 1
    else:
        return None if none==False else 0 
    
def GameOver2(finishers:list, board:list): # Slower
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
            return 1
        elif game_over and all(v==False for v in game_over):
            return -1
    else:
        return None if none==False else 0
