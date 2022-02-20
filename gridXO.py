class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row,column):
            if(row<0 or row==len(board) or column<0 or column==len(board[0]) or board[row][column]!='O'): 
                return 
            board[row][column]='E'
            dfs(row-1,column)
            dfs(row+1,column)
            dfs(row,column-1)
            dfs(row,column+1)
                
        for row in range(len(board)):
            for column in range(len(board[0])):
                if(board[row][column]=='O' and (row in [0,len(board)-1] or column in[0,len(board[0])-1])):
                    dfs(row,column)
        print(board)
        for row in range(len(board)):
            for column in range(len(board[0])):
                if(board[row][column]=='O'):
                    board[row][column]='X'
        for row in range(len(board)):
            for column in range(len(board[0])):
                if(board[row][column]=='E'):
                    board[row][column]='O'
        return board
                    
# Time complexity -  O(N^2)
        
