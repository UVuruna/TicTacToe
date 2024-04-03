from logic import TicTacToe
import threading
import random

class AI(threading.Thread,TicTacToe):
    none = None
    finishers = None
    board = None
    turn = None

    @staticmethod
    def Start(board,finishers,noneList,turn):
        AI.board     = board
        AI.finishers = finishers
        AI.none      = noneList
        AI.turn      = turn

        Threads = []
        for xy in noneList:
            t = AI(xy[0],xy[1])
            t.start()
            Threads.append(t)
        return Threads
    
    def __init__(self, x,y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y
        
        self.win = 0
        self.lose = 0
        self.draw = 0
        self.lose_in_one = False

    def run(self):
        Board = [line[:] for line in AI.board]
        self.Move(self.x,self.y,Board,AI.turn)
        
        none = list(AI.none)
        none.remove((self.x,self.y))
        n = len(none) ; N = int(n)-1
        end = self.GameOver(Board,AI.finishers,n)
        if end is not None:
            if (end==1 and AI.turn==1) or (end==-1 and AI.turn==-1):
                self.win+=1
                return
            elif (end==1 and AI.turn==-1) or (end==-1 and AI.turn==1):
                self.lose+=1
                return
            elif end==0:
                self.draw+=1
                return
            
        self.Score(none,n,Board,AI.turn*-1,end,N)

    def Score(self,none,n,board,turn,end,N):
        if (end==1 and self.turn==1) or (end==-1 and self.turn==-1):
            self.win+=1
            return
        elif (end==1 and self.turn==-1) or (end==-1 and self.turn==1):
            self.lose+=1
            if n==N:
                self.lose_in_one = True
            return
        elif end==0:
            self.draw+=1
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
            if not best:
                best.append((t.x,t.y))
                win_draw = (t.win+t.draw)/(t.win+t.lose+t.draw)
                win = t.win/(t.win+t.lose+t.draw)
                bestScore= win+win_draw
            else:
                win_draw = (t.win+t.draw)/(t.win+t.lose+t.draw)
                win = t.win/(t.win+t.lose+t.draw)
                score= win+win_draw
                if score>bestScore:
                    bestScore=score
                    best.clear()
                    best.append((t.x,t.y))
                elif score==bestScore:
                    best.append((t.x,t.y))
                    
        return best[0] if len(best)==1 else \
            random.choice(best) if len(best)>1 else\
            random.choice(([(t.x,t.y) for t in threads]))