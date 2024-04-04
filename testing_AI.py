import AI_multiprocessing as m
import AI_threading as t
from logic import TicTacToe
import time
from testing import Show_Matrix

def Analyze_Moves(aiList,bestmoveList,board,finishers,noneList,turn,PRINT):
    SUMA=[]
    for i,ai in enumerate(aiList):
        sum=0
        Threads = ai(board,finishers,noneList,turn)
        print(f'Best move: {bestmoveList[i](Threads) if bestmoveList[i].__module__!='AI_Basic' else bestmoveList[i](Threads,game.turn)}')
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
        else:
            SUMA.append(sum)
    return SUMA

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

def MakeThreads(board,finishers,noneList,turn):
    X = []
    print(noneList)
    for listN in noneList:
        x = improved.AI.Start(board,finishers,listN,turn)
        X+=x
    Analyze_Threads(X)

def Measuring_Execution_Time(ai:list,best_move:list,board,finishers,noneList,turn):
    print()
    for i,aiStart in enumerate(ai):
        start=time.time_ns()
        threads = aiStart(board,finishers,noneList,turn)
        best_move[i](threads,turn) if aiStart.__module__=='AI_Basic' else best_move[i](threads)
        end=time.time_ns()
        s = (end-start)/10**9
        print(f'{aiStart.__module__}'.ljust(13)+f'One execution: {s:,.3f} sec')
    print()

def Measuring_Time(board,finishers,noneList,turn):
        print()
        start=time.time_ns()
        threads = improved.AI.Start(board,finishers,noneList,turn)
        improved.AI.BestMove(threads,turn) if improved.AI.Start.__module__=='AI_Basic' else improved.AI.BestMove(threads)
        end=time.time_ns()
        s = (end-start)/10**9
        print(f'{improved.AI.Start.__module__}'.ljust(13)+f'One execution: {s:,.3f} sec')
        print()

if __name__=='__main__':
    game = TicTacToe(3)
    game.Move(1,1,game.board,game.turn) ; game.turn*=-1
    game.Move(0,0,game.board,game.turn) ; game.turn*=-1
    game.Move(2,0,game.board,game.turn) ; game.turn*=-1
    game.Move(0,2,game.board,game.turn) ; game.turn*=-1
    game.Move(0,1,game.board,game.turn) ; game.turn*=-1

    Show_Matrix(game.board)

    for clas in [m.Improved,m.Basic,m.Safe]:
        Total  = []
        for i in range(1):
            start = time.time_ns()
            xy = m.MultiAnalyze(clas,game.board,game.finishers,game.turn,game.None_Position())
            ende = time.time_ns()
            ms = (ende-start)/10**6
            Total.append(ms)
        else:
            print(f'\nTotal average {str(clas)[27:-2]} je: {sum(Total)/len(Total):,.2f} ms. Best move: {xy}')

    for clas in [t.Improved,t.Basic,t.Safe]:
        Total  = []
        for i in range(1000):
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

    
