class Solution(object):
    def numRookCaptures(self, board):
        n = 0
        m = 0
        count = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    n = i
                    m = j
                    
        for i in range(n - 1, -1, -1):
            if board[i][m] == "B":
                break
            elif board[i][m] == "p":
                count += 1
                break
    
        for i in range(n+1, 8):

            if board[i][m] == "B":
                break
            elif board[i][m] == "p":
                count += 1
                break
        for i in range(m-1, -1, -1):
            if board[n][i] == "B":
                break
            elif board[n][i] == "p":
                count += 1
                break
        for i in range(m+1,8):
            if board[n][i] == "B":
                break
            elif board[n][i] == "p":
                count += 1
                break 
        return count               

                
        
