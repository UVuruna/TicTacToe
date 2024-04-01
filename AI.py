
from logic import TicTacToe
from end_check import *
from testing import *
import random
import threading

# Namanja cifra Dobija za O i najveca za X
class AI(threading.Thread,TicTacToe):

    def __init__(self, x,y, game:TicTacToe):
        threading.Thread.__init__(self)
        self.x              = x
        self.y              = y
        self.score          = 0
        self.leafs          = 0
        self.lose_in_one    = False

    def Score(self,none,n,board,turn,end,N):
        if end is not None:
            self.score+=end
            self.leafs+=1
            if n==N:
                self.lose_in_one = True
            return
        for i in range(n):
            local_board = [line[:] for line in board] # Mnogo brze (>3*) od deepcopy
            local_none = none[:]
            local_turn = int(turn)
            x,y = local_none.pop(i)
            self.Move(x,y,local_board,local_turn)
            local_turn*=-1
            end = game.GameOver(local_board)

            self.Score(local_none,n-1,local_board,local_turn,end,N)

    def run(self):
        Board = [line[:] for line in game.board]
        turn = int(game.turn)
        self.Move(self.x,self.y,Board,turn)
        end = game.GameOver(Board)
        if end is not None:
            self.score+=1
            self.leafs+=1
            return

        none = game.None_Position(Board)
        n = len(none) ; N = int(n)-1
        self.Score(none,n,Board,turn*-1,end,N)

def AI_Start(none,game):
    Threads =[]
    for xy in none:
        t = AI(xy[0],xy[1],game)
        Threads.append(t)
        t.start()
    else:
        for t in Threads:
            t.join()
    return Threads

def Best_Move(moves_list):
    Moves_Dict=dict()
    for thread in moves_list:
        Moves_Dict[thread.x,thread.y]=100*thread.score/thread.leafs
    return Moves_Dict

def Analyze_Situation(funcTime=Measuring_Execution_Time,func1=AI_Start,func2=Best_Move):

    print(funcTime(func1,n=1,args=[none,game]),'\n')

    Threads = func1(none,game)
    sum=0
    for t in Threads:
        sum+=t.leafs
        print(f'({t.x},{t.y}) ima score: {t.score:,} sa {t.leafs:,} leafs. Lose in One: {t.lose_in_one}')
    print(f'\nUkupno poteza: {sum:,}.\n')

    Moves = func2(Threads)
    for k,v in Moves.items():
        print(f'potez: {k} : {v:.2f} %')


if __name__=='__main__':
    game = TicTacToe(3)
    #game.Move(1,1,game.board)
    #game.Move(2,2,game.board)
    #game.Move(1,2,game.board)
    #game.Move(2,1,game.board)
    #game.Move(0,1,game.board)
    Show_Matrix(game.board)

    #t = AI(1,2,game)
    #t2 = AI(2,1,game)
    none = game.None_Position()
    #'''

    Analyze_Situation()

