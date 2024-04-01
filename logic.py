
class TicTacToe:
    def __init__(self,boardXY,WinN=None) -> None:
        self.board_xy:int           = boardXY
        self.win_strike_number:int  = WinN if WinN!=None else 3 if boardXY<5 else 4 if boardXY<8 else 5
        self.finishers:list         = self.Finishers()
        self.board                  = self.Board_Create()
        self.turn                   = 1

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

        for i,line in enumerate(Diagonal_DR):
            x,y=Diagonal_DR[i][0]
            for i in range(1,self.board_xy-(x+y)):
                line.append((x+i,y+i))

        for i,line in enumerate(Diagonal_UR):
            x,y=Diagonal_UR[i][0]
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

    def GameOver(self,Board=False):
            # Vraca:
        # None ako je kraj partije bez pobednika
        #  1   ako je pobedio X
        # -1   ako je pobedio O
        #  0   ako niko nije pobedio (jos se igra)
        board = Board if Board else self.board
        finishers = self.finishers
        end = True
        for line in finishers:
            game_over = None
            for square in line:
                check = board[square[1]][square[0]]
                if check!=None:
                    if game_over is None:
                        game_over = board[square[1]][square[0]]
                    elif check!=game_over:
                        break
                else:
                    end = False
                    break
            else:
                return -1 if game_over==False else 1
        else:
            return None if end==False else 0 

    def GameOver2(self,Board=False):
            # Vraca:
        #  1   ako je pobedio X
        # -1   ako je pobedio O
        #  0   ako niko nije pobedio
        finishers = self.finishers
        board = Board if Board else self.board
        for line in finishers:
            game_over = None
            for square in line:
                check = board[square[1]][square[0]]
                if check!=None:
                    if game_over is None:
                        game_over = board[square[1]][square[0]]
                    elif check!=game_over:
                        break
                else:
                    break
            else:
                return -1 if game_over==False else 1
        else:
            return  0 

    def None_Position(self,board=None):
        NoneList=[]
        for y,line in enumerate(self.board if not board else board):
            for x,value in enumerate(line):
                if value is None:
                    NoneList.append((x,y))
        return NoneList

    def XO(self,turn=None):
        if not turn:
            return self.turn==1 # ili jos vise fensi return 'self.turn!=-1'
        else:
            return turn==1
        
    def Move(self,x,y,board,turn=None):
        if not turn:
            board[y][x] = self.XO()
            self.turn*=-1
        else:
            board[y][x] = self.XO(turn)


if __name__=='__main__':
    TicTac = TicTacToe(5)

    suma=0
    for i,v in enumerate(TicTac.Finishing_Lines()):
        suma+=1
        print(v)
    print(suma)