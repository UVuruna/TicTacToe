from GameLogic import *
import time

if __name__=='__main__':
    a = TicTacToe(3)
    print(MultiAnalyze(ImprovedM,a.board,a.finishers,a.turn,a.None_Position()))
    
    class Model:
        pass