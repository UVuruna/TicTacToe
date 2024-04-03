import AI_Basic as basic
import AI_Improved as improved
import AI_Safe as safe
from logic import TicTacToe
import testing as t
import time

def Analyze_Moves(aiList,bestmoveList,game,PRINT):
    SUMA=[]
    for i,ai in enumerate(aiList):
        sum=0
        Threads = ai(game)
        print(f'Best move: {bestmoveList[i](Threads) if bestmoveList[i].__module__!='AI_Basic' else bestmoveList[i](Threads,game.turn)}')
        for t in Threads:
            try:
                sum+=t.win+t.lose+t.draw
                local_sum = t.win+t.lose+t.draw
                if PRINT:
                    print(f'({t.x},{t.y}) win: {t.win:,} ({100*t.win/local_sum:.2f}%) ; draw: {t.draw:,} ({100*t.win/local_sum:.2f}%) ; lose: {t.lose:,} ({100*t.win/local_sum:.2f}%). Total {local_sum:,} leafs. Lose in One: {t.lose_in_one}')
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

def Measuring_Execution_Time(ai:list,best_move:list,game):
    print()
    for i,aiStart in enumerate(ai):
        start=time.time_ns()
        threads = aiStart(game)
        best_move[i](threads,game.turn) if aiStart.__module__=='AI_Basic' else best_move[i](threads)
        end=time.time_ns()
        s = (end-start)/10**9
        print(f'{aiStart.__module__}'.ljust(13)+f'One execution: {s:,.3f} sec')
    print()

if __name__=='__main__':
    game = TicTacToe(3)

    game.Move(1,1,game.board,game.turn) ; game.turn*=-1
    #game.Move(0,0,game.board,game.turn) ; game.turn*=-1
    #game.Move(1,0,game.board,game.turn) ; game.turn*=-1
    #game.Move(0,1,game.board,game.turn) ; game.turn*=-1
    #game.Move(0,2,game.board,game.turn) ; game.turn*=-1
    #game.Move(1,2,game.board,game.turn) ; game.turn*=-1
    #game.Move(2,1,game.board,game.turn) ; game.turn*=-1
    #game.Move(2,0,game.board,game.turn) ; game.turn*=-1
    print('--'*33+f'\nGame over: {game.GameOver(game.board,game.finishers,len(game.None_Position()))}\n')
    t.Show_Matrix(game.board)
    print()

    START = [basic.AI.Start,improved.AI.Start,safe.AI.Start]
    BEST = [basic.AI.BestMove,improved.AI.BestMove,safe.AI.BestMove]
    Measuring_Execution_Time(START,BEST,game)
    Analyze_Moves(START,BEST,game,True)

    '''
    ALL =[]
    for _ in range(30):
        all =Analyze_Moves(START,BEST,game,False)
        ALL.append(all)

    print(ALL)
    '''

    
