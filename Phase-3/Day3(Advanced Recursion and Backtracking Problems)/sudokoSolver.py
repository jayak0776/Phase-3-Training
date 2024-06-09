class Solution:
    def isPossible(self,x,y,board,value):
        #For checking row
        for col in range(9):
            if board[x][col]==str(value):
                return False
        #For checking col
        for row in range(9):
            if board[row][y]==str(value):
                return False
        #For checking block
        topRow=(x//3)*3
        topCol=(y//3)*3
        
        for i in range(3):
            for j in range(3):
                if board[topRow+i][topCol+j]==str(value):
                    return False
        return True     
    def solve(self,x,y,board):
        if x==9:
            return True
        
        nextX,nextY=-1,-1
        
        if y==8:
            nextX=x+1
            nextY=0
        else:
            nextX=x
            nextY=y+1    
            
        if board[x][y]!=".":
            return self.solve(nextX,nextY,board)
        
        for i in range(1,10):
            if self.isPossible(x,y,board,i)==True:
                board[x][y]=str(i)    
                result=self.solve(nextX,nextY,board)
                if result==True:
                    return True
                board[x][y]="."
                
        return False        
    
    
    
    def solveSudoku(self,board):
        self.solve(0,0,board)
        return board
        
    
board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]    
s=Solution()
print(s.solveSudoku(board))    