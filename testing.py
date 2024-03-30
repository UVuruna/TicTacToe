import time
import random
from logic import TicTacToe
from end_check import *


def Game_Simulation(game:TicTacToe,measuringTime=False):
    turn=1
    counter=0
    Time =[]
    while counter<(game.board_xy**2):
        x = random.randint(0,game.board_xy-1)
        y = random.randint(0,game.board_xy-1)
        while game.board[y][x] is not None:
            x = random.randint(0,game.board_xy-1)
            y = random.randint(0,game.board_xy-1)
        else:
            game.board[y][x] = True if turn==1 else False
            turn*=-1
            counter+=1
            end = GameOver(game.finishers,game.board)
            print(f'Ovo je stanje partije trenutno {end}')
            Show_Matrix(game.board)
            if measuringTime:
                t = MeasuringTime(GameOver,10**4,text=False,args=[game.finishers,game.board])
                Time.append(t)
                print(t,' ms')
            else:
                time.sleep(1)
            if end:
                return sum(Time)/len(Time)
    else:
        return sum(Time)/len(Time)

def Show_Matrix(matrix:list,countList=False,XO=True):
    if countList:
        print('Ima ih: ',len(matrix))
    print()
    for i in matrix:
        if XO is False:
            print(i)
        else:
            line = []
            for v in i:
                a= ' ' if v==None else 'X' if v==True else 'O'
                line.append(a)
            print(line)
    print()

def MeasuringTime(func,n=10**5,text=True,args:list=[]):
    start=time.time_ns()
    for _ in range(n):
        if not args:
            func()
        else:
            func(*args)
    end=time.time_ns()
    s = (end-start)/10**9
    ms = 10**6*s/n
    if text:
        return f'{func}\nOne run of function: {ms:,.3f} mikro sec\
                    \nTotal: {(end-start)/10**9:,.3f} s for {n:,.0f} runs'
    else:
        return ms

if __name__=='__main__':
    game1 = TicTacToe(7)
    print('Average time: ',Game_Simulation(game1,measuringTime=True),' ms')
