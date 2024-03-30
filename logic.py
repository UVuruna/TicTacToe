import time

class TicTacToe:
    def __init__(self,boardXY,WinN=None) -> None:
        self.board_xy:int           = boardXY
        self.win_strike_number:int  = WinN if WinN!=None else 3 if boardXY<5 else 4 if boardXY<8 else 5
        self.finishers:list         = self.Finishers()
        self.board                  = self.Board_Create()

    def Board_Create(self):
        Board = [[None]*self.board_xy for _ in range(self.board_xy)] # Table[0][1] je gornji srednji ; Table[1][2] je srednji desno
        return Board

    def Finishing_Lines(self):
        Horizontal, Vertical, Diagonal_DR, Diagonal_UR =[],[],[],[]
        startDiag = [x for x in range(self.board_xy-self.win_strike_number+1)]

        for y in range(self.board_xy):
            Horizontal.append([])
            Vertical.append([])
            for x in range(self.board_xy):
                Horizontal[y].append((x,y))
                Vertical[y].append((y,x))

                # Starting points for Diagonals
                if y in startDiag and x in startDiag and (x==0 or y==0):
                    Diagonal_DR.append([(x,y)]) 
                if x in startDiag and (self.board_xy-1-y) in startDiag and (x==0 or y==self.board_xy-1):
                    Diagonal_UR.append([(x,y)])

        for line in Diagonal_DR:
            x,y=Diagonal_DR[0][0]
            for i in range(1,self.board_xy-(x+y)):
                line.append((x+i,y+i))

        for line in Diagonal_UR:
            x,y=Diagonal_UR[0][0]
            for i in range(1,self.board_xy-(x+self.board_xy-1-y)):
                line.append((x+i,y-i))

        Lines =[] ; Lines += Horizontal ; Lines += Vertical ; Lines += Diagonal_DR ; Lines += Diagonal_UR 
        return Lines
    
    def Finishers(self):
        finishing_lines = self.Finishing_Lines()
        finishers=[]
        for line in finishing_lines:
            for i in range(len(line)):
                try:
                    line[self.win_strike_number+i-1]
                    finishers.append(line[i:self.win_strike_number+i])
                except IndexError:
                    break
        return finishers

    def GameOver(self):
            # Vraca:
        # None ako je kraj partije bez pobednika
        #  1   ako je pobedio X
        # -1   ako je pobedio O
        #  0   ako niko nije pobedio (jos se igra)
        none = False
        for line in self.finishers:
            game_over = []
            for square in line:
                check = self.board[square[1]][square[0]]
                if check!=None:
                    if game_over and check==game_over:
                        continue
                    elif game_over and check!=game_over and none==False:
                        continue # OVO NIJE DOBRO -- Razmisliti --
                    elif not game_over:
                        game_over = self.board[square[1]][square[0]]
                else:
                    none = True
                    break
            else:
                return -1 if game_over==False else 1
        else:
            return None if none==False else 0 
            pass # Videti za proveru da li ima None







    # TESTING FUNCTIONS

    def __Show_Finishers(self):
        print('Ima ih: ',len(self.finishers))
        for i in self.finishers:
            print(i)

    def __MeasuringTime(self,func,n=10**5):
        start=time.time_ns()
        for _ in range(n):
            func()
        end=time.time_ns()
        return f'{func}\nOne run of function: {10**6*(end-start)/(n*10**9):,.3f} mikro sec\
                    \nTotal: {(end-start)/10**9:,.3f} s for {n:,.0f} runs'

if __name__=='__main__':
    TicTac = TicTacToe(3)
    TicTac.board[0][1] = True
    print(TicTac.board)
    TicTac.GameOver()
    TicTac._TicTacToe__Show_Finishers()
    

    
    print(TicTac._TicTacToe__MeasuringTime(TicTac.Finishing_Lines))