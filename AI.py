from logic import TicTacToe
import random

class Improved(TicTacToe):
    def __init__(self, x,y, board,finishers,turn,none):
        self.x = x
        self.y = y
        self.board  = board
        self.finishers = finishers
        self.turn = turn
        self.none = none

        self.win = 0
        self.lose = 0
        self.draw = 0
        self.lose_in_one = False

    def run(self):
        Board = [line[:] for line in self.board]
        self.Move(self.x,self.y,Board,self.turn)
        self.none.remove((self.x,self.y))
        n = len(self.none) ; N = n-1
        end = self.GameOver(Board,self.finishers,n)
        if end is not None:
            if (end==1 and self.turn==1) or (end==-1 and self.turn==-1):
                self.win+=1
                return
            elif (end==1 and self.turn==-1) or (end==-1 and self.turn==1):
                self.lose+=1
                return
            elif end==0:
                self.draw+=1
                return
        self.Score(self.none,n,Board,self.turn*-1,end,N)

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
            end = self.GameOver(local_board,self.finishers,n-1)
            self.Score(local_none,n-1,local_board,local_turn,end,N) # RECURSION

    def BestMove(threads:list):
        best = list()
        bestScore:float
        for t in threads:
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
    
class Basic(TicTacToe):
    def __init__(self, x,y, board,finishers,turn,none):
        self.x = x
        self.y = y
        self.board  = board
        self.finishers = finishers
        self.turn = turn
        self.none = none

        self.score = 0
        self.leafs = 0
        self.lose_in_one = False

    def run(self):
        Board = [line[:] for line in self.board]
        self.Move(self.x,self.y,Board,self.turn)
        self.none.remove((self.x,self.y))
        n = len(self.none) ; N = n-1
        end = self.GameOver(Board,self.finishers,n)
        if end is not None:
            self.score+=1
            self.leafs+=1
            return
        self.Score(self.none,n,Board,self.turn*-1,end,N)

    def Score(self,none,n,board,turn,end,N):
        if end is not None:
            self.score+=end
            self.leafs+=1
            if n==N and ((end==-1 and self.turn==1) or (end==1 and self.turn==-1)):
                self.lose_in_one = True
            return
        for i in range(n):
            local_board = [line[:] for line in board] # Mnogo brze (>3*) od deepcopy
            local_none = none[:]
            local_turn = int(turn)
            x,y = local_none.pop(i)
            self.Move(x,y,local_board,local_turn)
            local_turn*=-1
            end = self.GameOver(local_board,self.finishers,n-1)
            self.Score(local_none,n-1,local_board,local_turn,end,N)

    def BestMove(threads:list,turn):
        best = list()
        bestScore:float
        for t in threads:
            if t.lose_in_one:
                continue
            if not best:
                best.append((t.x,t.y))
                bestScore = t.score/t.leafs
            else:
                score = t.score/t.leafs
                if (score>bestScore and turn==1) or (score<bestScore and turn==-1):
                    bestScore=score
                    best.clear()
                    best.append((t.x,t.y))
                elif score==bestScore:
                    best.append((t.x,t.y))
        return best[0] if len(best)==1 else \
            random.choice(best) if len(best)>1 else\
            random.choice(([(t.x,t.y) for t in threads]))
    
class Safe(TicTacToe):
    def __init__(self, x,y, board,finishers,turn,none):
        self.x = x
        self.y = y
        self.board  = board
        self.finishers = finishers
        self.turn = turn
        self.none = none

        self.win_in_one = False
        self.lose_in_one = False
        self.leafs = 0
        self.lose = 0

    def run(self):
        Board = [line[:] for line in self.board]
        self.Move(self.x,self.y,Board,self.turn)
        self.none.remove((self.x,self.y))
        n = len(self.none) ; N = int(n)-1
        end = self.GameOver(Board,self.finishers,n)
        if end is not None:
            if (end==1 and self.turn==1) or (end==-1 and self.turn==-1):
                self.win_in_one=True
                self.leafs+=1
                return
            elif (end==1 and self.turn==-1) or (end==-1 and self.turn==1):
                self.lose+=1
                self.leafs+=1
                return
        self.Score(self.none,n,Board,self.turn*-1,end,N)

    def Score(self,none,n,board,turn,end,N):
        if end is not None:
            self.leafs+=1
            if (end==1 and self.turn==-1) or (end==-1 and self.turn==1):
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
            end = self.GameOver(local_board,self.finishers,n-1)
            self.Score(local_none,n-1,local_board,local_turn,end,N)
    
    def BestMove(threads:list):
        best = list()
        bestScore:float
        for t in threads:
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