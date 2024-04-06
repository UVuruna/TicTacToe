import time
import random
from Logic import TicTacToe

def Game_Simulation(pc1,pc2,PRINT):
    game = TicTacToe(3)
    end=None

    while end is None:
        ts = time.time_ns() # <<<
        if game.turn==1:
            threads=pc1.Start(game)
            x,y=pc1.BestMove(threads,game.turn) if pc1.__module__=='AI_Basic' else pc1.BestMove(threads)

        else:
            threads=pc2.Start(game)
            x,y=pc2.BestMove(threads,game.turn) if pc2.__module__=='AI_Basic' else pc2.BestMove(threads)

        game.Move(x,y,game.board,game.turn)
        game.turn*=-1
        end = game.GameOver(game.board,game.finishers,len(game.None_Position()))

        te = time.time_ns() # <<<
        if PRINT:
            print(f'\nX: {pc1.__module__}: execution = {(te-ts)/10**6:,.2f} ms ; best move = {x,y}' if game.turn==-1 else\
                f'\nO: {pc2.__module__}: execution = {(te-ts)/10**6:,.2f} ms ; best move = {x,y}')
            Show_Matrix(game.board)
    else:
        kraj = 'X-WIN' if end==1 else 'O-WIN' if end==-1 else 'DRAW'
        print(f'\nPartija zavrsena: {kraj}\n')

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

def Measuring_Execution_Time(func,n=10**5,text=True,args:list=[],iter=False): # za game over je sluzilo
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

def Yield_Total_Combinations(s:set): # Bezveze
    for i in sorted(s):
        yield i
        s.remove(i)
        for j in Yield_Total_Combinations(s):
            yield i+j
        s.add(i)

def List_Total_Combinations(s:list, results:list):  # Bezveze
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

def FunctionTiming(func:callable,n,unit,*args):
    ts = time.time_ns()
    for _ in range(n):
        func(*args)
    te = time.time_ns()
    coef = 1 if unit=='ns' else 10**3 if unit=='micro s' else 10**6 if unit=='ms' else 10**9
    print(f'{(te-ts)/(n*coef):,.2f} {unit}')


if __name__=='__main__':

    game1 = TicTacToe(3)
    #Game_Simulation(basicM.AI,ai.safe.AI,game1)

    #FunctionTiming(Total_Combinations_up_to_Level,10**5,'micro s',25,4)
    #FunctionTiming(Game_Simulation,30,'s',ai.improved.AI,ai.improved.AI,False)
    #print(f'{Total_Combinations_up_to_Level(25,25):,}')





