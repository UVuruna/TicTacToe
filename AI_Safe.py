
from logic import TicTacToe
import threading
import random


# IF WIN == TRUE Play this MOVE else choose MOVE with the least chance for LOSE
class AI(threading.Thread,TicTacToe):
    none = None
    finishers = None
    board = None
    turn = None

    @staticmethod
    def Start(game:TicTacToe):
        AI.board = game.board
        AI.none = game.None_Position(AI.board)
        AI.finishers = game.finishers
        AI.turn = game.turn
        Threads = []

        for xy in AI.none:
            instance_none = list(AI.none)
            instance_none.remove((xy[0],xy[1]))
            t = AI(xy[0],xy[1],instance_none)
            t.start()
            Threads.append(t)
        return Threads

    def __init__(self, x,y, game:TicTacToe):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y

        self.win_in_one = False
        self.lose_in_one = False
        self.leafs = 0
        self.lose = 0

    def run(self):
        Board = [line[:] for line in AI.board]
        turn = int(AI.turn)
        self.Move(self.x,self.y,Board,turn)

        none = list(AI.none)
        none.remove((self.x,self.y))
        n = len(none) ; N = int(n)-1
        end = self.GameOver(Board,AI.finishers,n)

        if end is not None:
            if (end==1 and AI.turn==1) or (end==-1 and AI.turn==-1):
                self.win_in_one=True
                self.leafs+=1
                return
            elif (end==1 and AI.turn==-1) or (end==-1 and AI.turn==1):
                self.lose+=1
                self.leafs+=1
                return
    
        self.Score(none,n,Board,turn*-1,end,N)

    def Score(self,none,n,board,turn,end,N):
        if end is not None:
            self.leafs+=1
            if (end==1 and AI.turn==-1) or (end==-1 and AI.turn==1):
                self.lose+=1
                if n==N:
                    self.lose_in_one = True
            return
        for i in range(n):
            local_board = [line[:] for line in board]
            local_none = none[:]
            local_turn = int(turn)
            x,y = local_none.pop(i)
            self.Move(x,y,local_board,local_turn)
            local_turn*=-1
            end = self.GameOver(local_board,AI.finishers,n-1)
            
            self.Score(local_none,n-1,local_board,local_turn,end,N)
    
    def BestMove(threads:list):
        best = list()
        bestScore:float
        for t in threads:
            t.join()
            if t.lose_in_one:
                continue
            if t.win_in_one:
                return (t.x,t.y)
            if not best:
                best.append((t.x,t.y))
                bestScore = t.lose/t.leafs
            else:
                score = t.lose/t.leafs
                if score<bestScore:
                    bestScore=score
                    best.clear()
                    best.append((t.x,t.y))
                elif score==bestScore:
                    best.append((t.x,t.y))

        return best[0] if len(best)==1 else \
            random.choice(best) if len(best)>1 else\
            random.choice(([(t.x,t.y) for t in threads]))