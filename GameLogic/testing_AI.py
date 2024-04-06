from AI_Multiprocessing import *
from AI_Threading import *
from Logic import TicTacToe
import time
from testing import Show_Matrix

def AverageTime(func,n,*args):
    TIME = []
    for _ in range(n):
        t1 = time.time_ns()
        func(*args)
        t2 = time.time_ns()
        TIME.append((t2-t1)/10**6)
    return TIME


def Analyze_Threads(Threads,PRINT=True):
    SUMA=[]
    sum=0
    for t in Threads:
        try:
            sum+=t.win+t.lose+t.draw
            local_sum = t.win+t.lose+t.draw
            if PRINT:
                print(f'({t.x},{t.y}) win: {t.win:,} ({100*t.win/local_sum:.2f}%) ; draw: {t.draw:,} ({100*t.draw/local_sum:.2f}%) ; lose: {t.lose:,} ({100*t.lose/local_sum:.2f}%). Total {local_sum:,} leafs. Lose in One: {t.lose_in_one}')
        except AttributeError:
            sum+=t.leafs
            if PRINT:
                try:
                    print(f'({t.x},{t.y}) ima score: {t.score:,} ({100*t.score/t.leafs:.2f}%). Total {t.leafs:,} leafs. Lose in One: {t.lose_in_one}')
                except AttributeError:
                    print(f'({t.x},{t.y}) lose: {100*t.lose/t.leafs:.2f}%. Total {t.leafs:,} leafs. Win in One:{t.win_in_one}. Lose in One: {t.lose_in_one}')
    if PRINT:
        print(f'Ukupno poteza: {sum:,}.')
        print()


def Measuring_Execution_Time(ai:list,board,finishers,noneList,turn,type='Multiprocess'):
    print()
    if type=='Threading':
        for aiStart in ai:
            start=time.time_ns()
            threads = aiStart.Start(board,finishers,turn,noneList)
            xy = aiStart.BestMove(threads)
            end=time.time_ns()
            s = (end-start)/10**6
            print(f'{str(aiStart)[:]}  One execution: {s:,.2f} ms. Best Move: {xy}')
    else:
        for aiStart in ai:
            start=time.time_ns()
            xy = MultiAnalyze(aiStart,board,finishers,turn,noneList)
            end=time.time_ns()
            s = (end-start)/10**6
            print(f'{str(aiStart)[:]}  One execution: {s:,.2f} ms. Best Move: {xy}')
    print()

if __name__=='__main__':
    game = TicTacToe(3)
    game.Move(1,1,game.board,game.turn) ; game.turn*=-1
    #game.Move(0,0,game.board,game.turn) ; game.turn*=-1
    #game.Move(2,0,game.board,game.turn) ; game.turn*=-1
    #game.Move(0,2,game.board,game.turn) ; game.turn*=-1
    #game.Move(0,1,game.board,game.turn) ; game.turn*=-1
    #game.Move(2,1,game.board,game.turn) ; game.turn*=-1

    Show_Matrix(game.board)

    Measuring_Execution_Time([ImprovedM,BasicM,SafeM],game.board,game.finishers,game.None_Position(),game.turn)
    Measuring_Execution_Time([ImprovedT,BasicT,SafeT],game.board,game.finishers,game.None_Position(),game.turn,'Threading')



    '''
    for clas in [BasicM,ImprovedM,SafeM]:
        Total  = []
        for i in range(1):
            start = time.time_ns()
            xy,result = MultiAnalyze(clas,game.board,game.finishers,game.turn,game.None_Position())
            #Analyze_Threads(result)
            ende = time.time_ns()
            ms = (ende-start)/10**6
            Total.append(ms)
        else:
            print(f'Total average {str(clas)[27:-2]} je: {sum(Total)/len(Total):,.2f} ms. Best move: {xy}')
        
    
    
    for clas in [ImprovedT,BasicT,SafeT]:
        Total  = []
        for i in range(1):
            start = time.time_ns()
            List = clas.Start(game.board,game.finishers,game.turn,game.None_Position())
            xy = clas.BestMove(List) if str(clas)[21:-2]!='Basic' else clas.BestMove(List,game.turn)
            ende = time.time_ns()
            #Analyze_Threads(List)
            ms = (ende-start)/10**6
            Total.append(ms)
        else:
            print(f'\nTotal average {str(clas)[21:-2]} je: {sum(Total)/len(Total):,.2f} ms. Best move: {xy}')
    '''
            
    '''
    game = TicTacToe(3)

    game.Move(1,1,game.board,game.turn) ; game.turn*=-1
    game.Move(0,0,game.board,game.turn) ; game.turn*=-1
    game.Move(1,0,game.board,game.turn) ; game.turn*=-1
    #game.Move(0,1,game.board,game.turn) ; game.turn*=-1
    #game.Move(0,2,game.board,game.turn) ; game.turn*=-1
    #game.Move(1,2,game.board,game.turn) ; game.turn*=-1
    #game.Move(2,1,game.board,game.turn) ; game.turn*=-1
    #game.Move(2,0,game.board,game.turn) ; game.turn*=-1


    noneList = game.None_Position()
    START = [basic.AI.Start,improved.AI.Start,safe.AI.Start]
    BEST = [basic.AI.BestMove,improved.AI.BestMove,safe.AI.BestMove]
    Measuring_Execution_Time(START,BEST,game.board,game.finishers,noneList,game.turn)
    Analyze_Moves(START,BEST,game.board,game.finishers,noneList,game.turn,True)
    '''

    '''
    ALL =[]
    for _ in range(30):
        all =Analyze_Moves(START,BEST,game,False)
        ALL.append(all)

    print(ALL)
        '''

    
