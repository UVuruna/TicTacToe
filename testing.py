import time
import random
from logic import TicTacToe
from end_check import *


def Game_Simulation(game:TicTacToe,measuringTime=False):
    counter=0
    Time =[]
    Time2 =[]
    while counter<(game.board_xy**2):
        x = random.randint(0,game.board_xy-1)
        y = random.randint(0,game.board_xy-1)
        while game.board[y][x] is not None:
            x = random.randint(0,game.board_xy-1)
            y = random.randint(0,game.board_xy-1)
        else:
            game.Move(x,y)
            counter+=1
            end2 = GameOver2(game.finishers,game.board)
            end = game.GameOver()
            print(f'\n\nOvo je stanje partije trenutno {counter}. potez:\n\t{end} (GameOver) ; {end2} (GameOver2)')
            Show_Matrix(game.board)
            if measuringTime:
                t2 = Measuring_Execution_Time(game.GameOver2,10**5,text=False)
                Time2.append(t2)
                t = Measuring_Execution_Time(game.GameOver,10**5,text=False)
                Time.append(t)
                print(f'\t{t:,.3f} ms (GameOver) ; {t2:,.3f} ms (GameOver2)'
                      f'\n\tza {abs((t2 if t2>t else t)/(t if t2>t else t2))*100-100:,.2f}% je {'GameOver' if t2>t else 'GameOver2'} brzi')
            else:
                time.sleep(1)
            if end:
                return sum(Time)/len(Time),sum(Time2)/len(Time2)
    else:
        return sum(Time)/len(Time),sum(Time2)/len(Time2)

def Show_Matrix(matrix:list,countList=False,XO=True):
    if countList:
        print('Ima ih: ',len(matrix))
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

def Measuring_Execution_Time(func,n=10**5,text=True,args:list=[],iter=False):
    start=time.time_ns()
    for _ in range(n):
        if not args:
            func()
        else:
            a=func(*args)
            if iter:
                Lista=[]
                for i in a:
                    Lista.append(i)
    end=time.time_ns()
    s = (end-start)/10**9
    ms = 10**6*s/n
    if text:
        return f'{func}\nOne run of function: {ms:,.3f} mikro sec\
                    \nTotal: {(end-start)/10**9:,.3f} s for {n:,.0f} runs'
    else:
        return ms

def Showcase_Print(func:callable,*args):
    print(f'{func} {args}: {func(*args):,}')

def Yield_Total_Combinations(s:set):
    for i in sorted(s):
        yield i
        s.remove(i)
        for j in Yield_Total_Combinations(s):
            yield i+j
        s.add(i)

def List_Total_Combinations(s:list, results:list):
    for i in range(len(s)):
        results.append(s[i])
        tempset = s[:]
        del tempset[i]
        tempresults = []
        List_Total_Combinations(tempset, tempresults)
        for res in tempresults:
            results.append(s[i] + res)

def Total_Combinations(n):
    if n==1: # moze n==0 then return 0
        return 1
    return Total_Combinations(n-1)*n+n

def Total_Leafs_PerLevel(N,n): # last 2 levels == same leaf number ; N==Depth ; n==Level
    if n==1: # moze n==0 then return 1
        return N
    return Total_Leafs_PerLevel(N,n-1)*(N+1-n)

def Total_Combinations_up_to_Level(N,n):
    suma=0
    for i in range(1,n+1):
        suma+=Total_Leafs_PerLevel(N,i)
    return suma

def Showcase(func:callable,*args):
    print(f'{func} {args}: {func(*args):,}')

counter=0
def Combination_Tree(n,lista): # n == sum count None
    global counter
    if n==0: 
        return
    for i in range(n):
        local_list=lista[:] # local_list = copy.deepcopy(lista)
        print(f'Izlazi: {local_list.pop(i)} ; ostatak liste: {local_list}')
        #time.sleep(0.01)
        counter+=1
        Combination_Tree(n-1,local_list)



if __name__=='__main__':

    game1 = TicTacToe(3)
    t,t2 = Game_Simulation(game1,measuringTime=True)
    print('\n   Prosek partije:')
    print(f'Average time: {t:,.2f} ms (GameOver)')
    print(f'Average time: {t2:,.2f} ms (GameOver2)')
    print(f'za {abs((t2 if t2>t else t)/(t if t2>t else t2))*100-100:,.2f}% je {'GameOver' if t2>t else 'GameOver2'} brzi')





