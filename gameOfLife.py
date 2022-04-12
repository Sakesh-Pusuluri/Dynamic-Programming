class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        corners=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,1),(1,0),(1,-1)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                val = self.updateValue(row,col,corners,board)
                if(board[row][col]!=val):
                    if(val==1):
                        board[row][col]='a'
                    else:
                        board[row][col]='b'
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col]=='a'):
                    board[row][col]=1
                elif(board[row][col]=='b'):
                    board[row][col]=0    
        return board
        
    def updateValue(self,row,col,corners,board):
        _sum=0
        for i,j in corners:
            updatedRow,updatedCol = row+i,col-j
            if(updatedRow>=0 and updatedRow<len(board) and updatedCol>=0 and updatedCol<len(board[0])):
                if(board[updatedRow][updatedCol]=='a'):
                    _sum += 0
                elif(board[updatedRow][updatedCol]=='b'):
                    _sum+=1
                else:
                    _sum+=board[updatedRow][updatedCol]
        if(board[row][col]==0):
            if(_sum==3):
                return 1
            else:
                return 0
        else:
            if(_sum<2):
                return 0
            elif(_sum==2 or _sum==3):
                return 1
            else:
                return 0
                
                
            
        
