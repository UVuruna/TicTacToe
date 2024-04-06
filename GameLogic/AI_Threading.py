try:
    from GameLogic.Logic import TicTacToe
except ModuleNotFoundError:
    from Logic import TicTacToe
import threading
import random

class BasicT(threading.Thread,TicTacToe):
    none = None
    finishers = None
    board = None
    turn = None

    @staticmethod
    def Start(board,finishers,turn,noneList):
        BasicT.board = board
        BasicT.finishers = finishers
        BasicT.none = noneList
        BasicT.turn = turn

        Threads = []
        for xy in noneList:
            t = BasicT(xy[0],xy[1])
            t.start()
            Threads.append(t)
        return Threads

    def __init__(self, x,y):
        threading.Thread.__init__(self)
        self.x              = x
        self.y              = y

        self.score          = 0
        self.leafs          = 0
        self.lose_in_one    = False

    def run(self):
        Board = [line[:] for line in BasicT.board]
        self.Move(self.x,self.y,Board,BasicT.turn)
        none = BasicT.none[:]
        none.remove((self.x,self.y))
        n = len(none)
        end = self.GameOver(Board,BasicT.finishers,n)
        if end is not None:
            self.score+=1
            self.leafs+=1
            return
        self.Score(none,n,Board,BasicT.turn*-1,end,n-1)

    def Score(self,none,n,board,turn,end,N):
        if end is not None:
            self.score+=end
            self.leafs+=1
            if n==N and ((end==-1 and BasicT.turn==1) or (end==1 and BasicT.turn==-1)):
                self.lose_in_one = True
            return
        for i in range(n):
            local_board = [line[:] for line in board] # Mnogo brze (>3*) od deepcopy
            local_none = none[:]
            x,y = local_none.pop(i)
            self.Move(x,y,local_board,turn)
            local_turn = turn*-1
            end = self.GameOver(local_board,BasicT.finishers,n-1)
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
                bestScore = t.score/t.leafs
            else:
                score = t.score/t.leafs
                if (score>bestScore and BasicT.turn==1) or (score<bestScore and BasicT.turn==-1):
                    bestScore=score
                    best.clear()
                    best.append((t.x,t.y))
                elif score==bestScore:
                    best.append((t.x,t.y))
        return best[0] if len(best)==1 else \
            random.choice(best) if len(best)>1 else\
            random.choice(([(t.x,t.y) for t in threads]))
    
class ImprovedT(threading.Thread,TicTacToe):
    none = None
    finishers = None
    board = None
    turn = None

    @staticmethod
    def Start(board,finishers,turn,noneList):
        ImprovedT.board     = board
        ImprovedT.finishers = finishers
        ImprovedT.none      = noneList
        ImprovedT.turn      = turn

        Threads = []
        for xy in noneList:
            t = ImprovedT(xy[0],xy[1])
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
        Board = [line[:] for line in ImprovedT.board]
        self.Move(self.x,self.y,Board,ImprovedT.turn)
        none = ImprovedT.none[:]
        none.remove((self.x,self.y))
        n = len(none)
        end = self.GameOver(Board,ImprovedT.finishers,n)
        if end is not None:
            if (end==1 and ImprovedT.turn==1) or (end==-1 and ImprovedT.turn==-1):
                self.win+=1
                return
            elif (end==1 and ImprovedT.turn==-1) or (end==-1 and ImprovedT.turn==1):
                self.lose+=1
                return
            elif end==0:
                self.draw+=1
                return
        self.Score(none,n,Board,ImprovedT.turn*-1,end,n-1)

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
            x,y = local_none.pop(i)
            self.Move(x,y,local_board,turn)
            local_turn = turn*-1
            end = self.GameOver(local_board,ImprovedT.finishers,n-1)
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

class SafeT(threading.Thread,TicTacToe):
    none = None
    finishers = None
    board = None
    turn = None

    @staticmethod
    def Start(board,finishers,turn,noneList):
        SafeT.board = board
        SafeT.finishers = finishers
        SafeT.none = noneList
        SafeT.turn = turn

        Threads = []
        for xy in noneList:
            t = SafeT(xy[0],xy[1])
            t.start()
            Threads.append(t)
        return Threads

    def __init__(self, x,y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y

        self.win_in_one = False
        self.lose_in_one = False
        self.leafs = 0
        self.lose = 0

    def run(self):
        Board = [line[:] for line in SafeT.board]
        self.Move(self.x,self.y,Board,SafeT.turn)
        none = SafeT.none[:]
        none.remove((self.x,self.y))
        n = len(none)
        end = self.GameOver(Board,SafeT.finishers,n)
        if end is not None:
            if (end==1 and SafeT.turn==1) or (end==-1 and SafeT.turn==-1):
                self.win_in_one=True
                self.leafs+=1
                return
            elif (end==1 and SafeT.turn==-1) or (end==-1 and SafeT.turn==1):
                self.lose+=1
                self.leafs+=1
                return
        self.Score(none,n,Board,SafeT.turn*-1,end,n-1)

    def Score(self,none,n,board,turn,end,N):
        if end is not None:
            self.leafs+=1
            if (end==1 and SafeT.turn==-1) or (end==-1 and SafeT.turn==1):
                self.lose+=1
                if n==N:
                    self.lose_in_one = True
            return
        for i in range(n):
            local_board = [line[:] for line in board]
            local_none = none[:]
            x,y = local_none.pop(i)
            self.Move(x,y,local_board,turn)
            local_turn = turn*-1
            end = self.GameOver(local_board,SafeT.finishers,n-1)    
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