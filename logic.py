
class TicTacToe:
    finishers = None
    def __init__(self,scale,WinN=None) -> None:
        self.scale:int              = scale
        self.win_sequence:int       = WinN if WinN!=None else 3 if scale<5 else 4 if scale<8 else 5
        self.finishers:list         = self.Finishers()
        self.board                  = self.Board_Create()
        self.turn                   = 1

    def Board_Create(self):
        Board = [[None]*self.scale for _ in range(self.scale)]
        return Board

    def Finishing_Lines(self):
        Horizontal, Vertical, Diagonal_Down, Diagonal_Up =[],[],[],[]
        diagonal_corners = [x for x in range(self.scale-self.win_sequence+1)]

        for y in range(self.scale):
            Horizontal.append([])
            Vertical.append([])
            for x in range(self.scale):
                Horizontal[y].append((x,y))
                Vertical[y].append((y,x))
                    # Starting points for Diagonals
                if y in diagonal_corners and x in diagonal_corners and (x==0 or y==0):
                    Diagonal_Down.append([(x,y)]) 
                if x in diagonal_corners and (self.scale-1-y) in diagonal_corners and (x==0 or y==self.scale-1):
                    Diagonal_Up.append([(x,y)])

        for i,line in enumerate(Diagonal_Down):
            x,y=Diagonal_Down[i][0]
            for i in range(1,self.scale-(x+y)):
                line.append((x+i,y+i))

        for i,line in enumerate(Diagonal_Up):
            x,y=Diagonal_Up[i][0]
            for i in range(1,self.scale-(x+self.scale-1-y)):
                line.append((x+i,y-i))

        return Horizontal+Vertical+Diagonal_Down+Diagonal_Up
    
    def Finishers(self):
        finishing_lines = self.Finishing_Lines()
        finishers=[]
        for line in finishing_lines:
            for i in range(len(line)):
                try:
                    line[self.win_sequence+i-1]
                    finishers.append(line[i:self.win_sequence+i])
                except IndexError:
                    break
        return finishers

    def GameOver(self,board,finishers,none):
        for line in finishers:
            game_over = None
            for square in line:
                check = board[square[1]][square[0]]
                if check!=None:
                    if game_over is None:
                        game_over = check
                    elif check!=game_over:
                        break
                else:
                    break
            else:
                return 1 if game_over else -1
        return None if none else 0
    
    def Evaluate(self,board,finishers,none):
        for line in finishers:
            game_over = list()
            for square in line:
                check = board[square[1]][square[0]]
                game_over.append(check)
            else:
                return 1 if game_over else -1
        return None if none else 0

    def None_Position(self,board=None):
        NoneList=[]
        for y,line in enumerate(self.board if not board else board):
            for x,value in enumerate(line):
                if value is None:
                    NoneList.append((x,y))
        return NoneList
        
    def Move(self,x,y,board,turn):
        board[y][x] = turn==1

    def Horizontal_Lvl(self,N,n):
        if n==1:
            return N
        return self.Horizontal_Lvl(N,n-1)*(N+1-n)

    def Total_upTo_Horizontal_Lvl(self,N,n):
        suma=0
        for i in range(1,n+1):
            suma+=self.Horizontal_Lvl(N,i)
        return suma

    def Optimal_Work(self):
        none = len(self.None_Position())
        for n in range(3,none+1):
            x = self.Horizontal_Lvl(none,n)
            if x>3*10**6:
                return n if x<7*10**6 else n-1

            
if __name__=='__main__':
    TicTac = TicTacToe(5)
    #for i in TicTac.Finishing_Lines():
        #print(i)

    depth = TicTac.Optimal_Work()
    print(f'{depth} levels deep')
    print(f'{TicTac.Horizontal_Lvl(49,4):,}')
    print(f'{TicTac.Horizontal_Lvl(20,5):,}')