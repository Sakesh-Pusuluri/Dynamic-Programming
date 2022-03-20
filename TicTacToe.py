class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.mat =[[n+1]*n for i in range(n) ]
        
    def checkRow(self,row):
        _sum = 0
        for i in range(self.n):
            _sum +=self.mat[row][i]
        if(_sum == self.n or _sum == 0):
            return True
        return False
    def checkColumn(self,column):
        _sum = 0
        for i in range(self.n):
            _sum +=self.mat[i][column]
        if(_sum == self.n or _sum == 0):
            return True
        return False
    def checkDiagonal(self):
        _sum = 0
        for i in range(self.n):
            _sum +=self.mat[i][i]
        if(_sum == self.n or _sum == 0):
            return True
        return False
    def reverseDiagonal(self):
        _sum=0
        i,j=0,self.n-1
        for idx in range(self.n):
            _sum += self.mat[i][j]
            i +=1
            j -= 1
        if(_sum == self.n or _sum == 0):
            return True
        return False
        

    def move(self, row: int, col: int, player: int) -> int:
        if(player==1):
            self.mat[row][col] = 1
        else: 
            self.mat[row][col] = 0
        if(self.checkRow(row) or self.checkColumn(col) or self.checkDiagonal() or self.reverseDiagonal()):
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
