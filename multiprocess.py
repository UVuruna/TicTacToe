
import multiprocessing
import AI
import logic as l
import time

# 3 puta BRZE 
# 350 ms za prazan board 3x3, 255,168 resenja (vise od toga radi) ; 986,409 poteza (manje od toga radi)
# bez multiprocessing 1,000 ms

def worker(thread):
    thread.run()
    return thread

def MultiAnalyze(AI,board,finishers,turn,none,BASIC=False):
    Threads = []
    for xy in none:
        t = AI(xy[0],xy[1],board,finishers,turn,none)
        Threads.append(t)

    with multiprocessing.Manager() as manager:
        shared_list = manager.list(Threads)

        with multiprocessing.Pool(processes=16) as pool:
            result = pool.map(worker, shared_list)

    xy = AI.BestMove(result) if str(AI)!="<class 'AI.Basic'>" else AI.BestMove(result,turn)
    return xy

if __name__ == '__main__':
    game = l.TicTacToe(3)

    Total  = []
    for clas in [AI.Improved,AI.Basic,AI.Safe]:
        for i in range(500):
            start = time.time_ns()
            xy = MultiAnalyze(clas,game.board,game.finishers,game.turn,game.None_Position(),BASIC=False)
            ende = time.time_ns()
            ms = (ende-start)/10**6
            Total.append(ms)
        else:
            print(f'\nTotal average je: {sum(Total)/len(Total):,.2f} ms')