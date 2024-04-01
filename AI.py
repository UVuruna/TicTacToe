
from logic import TicTacToe
from end_check import *
from testing import *
import threading

class AI(threading.Thread,TicTacToe):

    def __init__(self, x,y, game:TicTacToe):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y
        self.score = 0
        self.leafs = 0
        self.turn = int(game.turn)
        self.board = [line[:] for line in game.board]
        self.board_xy = game.board_xy
        self.finishers = game.finishers

    def Score(self,none,n,board,turn):
        for i in range(n):
            local_board = [line[:] for line in board] # Mnogo brze (>3*) od deepcopy
            local_none = none[:]
            local_turn = int(turn)
            x,y = local_none.pop(i)
            self.Move(x,y,local_board,local_turn)
            local_turn*=-1
            end = self.GameOver(local_board)
            if end is not None:
                self.score+=end
                self.leafs+=1
                return
            self.Score(local_none,n-1,local_board,local_turn)

    def run(self):
        self.Move(self.x,self.y,self.board)
        end = self.GameOver()
        if end is None:
            none = self.None_Position()
            self.Score(none,len(none),self.board,self.turn)
        else:
            self.score+=1
            self.leafs+=1

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

if __name__=='__main__':
    game = TicTacToe(3)
    game.Move(1,1,game.board)
    #game.Move(2,2,game.board)
    #game.Move(1,2,game.board)
    #game.Move(2,1,game.board)
    #game.Move(0,1,game.board)
    Show_Matrix(game.board)

    #t = AI(1,2,game)
    #t2 = AI(2,1,game)
    none = game.None_Position()
    #'''
    print(Measuring_Execution_Time(AI_Start,n=1,args=[none,game]))
    Threads = AI_Start(none,game)
    for t in Threads:
        print(f'({t.x},{t.y}) ima score: {t.score} sa {t.leafs} leafs')

    Moves = Best_Move(Threads)
    for k,v in Moves.items():
        print(f'potez: {k} : {v:.2f} %')
        #'''

