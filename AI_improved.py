
from logic import TicTacToe
from end_check import *
from testing import *
import threading

class AI(threading.Thread,TicTacToe):

    def __init__(self, x,y, game:TicTacToe):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y
        self.win = 0
        self.lose = 0
        self.draw = 0

    def Score(self,none,n,board,turn):
        for i in range(n):
            local_board = [line[:] for line in board]
            local_none = none[:]
            local_turn = int(turn)
            x,y = local_none.pop(i)
            self.Move(x,y,local_board,local_turn)
            local_turn*=-1
            end = game.GameOver(local_board)
            if (end==1 and game.turn==1) or (end==-1 and game.turn==-1):
                self.win+=1
                return
            elif (end==1 and game.turn==-1) or (end==-1 and game.turn==1):
                self.lose+=1
                return
            elif end==0:
                self.draw+=1
                return
            self.Score(local_none,n-1,local_board,local_turn)

    def run(self):
        Board = [line[:] for line in game.board]
        turn = int(game.turn)
        self.Move(self.x,self.y,Board,turn)
        end = game.GameOver(Board)
        if end is None:
            none = game.None_Position(Board)
            self.Score(none,len(none),Board,turn*-1)
        else:
            if (end==1 and game.turn==1) or (end==-1 and game.turn==-1):
                self.win+=1
                return
            elif (end==1 and game.turn==-1) or (end==-1 and game.turn==1):
                self.lose+=1
                return
            elif end==0:
                self.draw+=1
                return

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
        sum = thread.win+thread.lose+thread.draw
        win = 100*thread.win/sum
        lose = 100*thread.lose/sum
        draw = 100*thread.draw/sum
        Moves_Dict[thread.x,thread.y]=[win,draw,lose]
    return Moves_Dict

if __name__=='__main__':
    game = TicTacToe(3)
    
    game.Move(1,1,game.board)
    game.Move(2,2,game.board)
    game.Move(1,0,game.board)
    game.Move(1,2,game.board)
    game.Move(0,2,game.board)
    game.Move(2,0,game.board)
    print(game.turn)
    Show_Matrix(game.board)

    #t = AI(1,2,game)
    #t2 = AI(2,1,game)
    none = game.None_Position()
    #'''
    print(Measuring_Execution_Time(AI_Start,n=1,args=[none,game]))
    Threads = AI_Start(none,game)
    for t in Threads:
        print(f'({t.x},{t.y}) >> win: {t.win} ; draw: {t.draw} ; lose: {t.lose} <<\n')

    Moves = Best_Move(Threads)
    for k,v in Moves.items():
        print(f'potez: {k} = win: {v[0]:.2f}%; draw: {v[1]:.2f}%; lose: {v[2]:.2f}%')

