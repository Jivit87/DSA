class Solution(object):
    def numSpecial(self, mat):
        m = len(mat)
        n = len(mat[0])
        def row(row):
            if sum(mat[row]) == 1:
                return True
            else:
                return False   
        def col(c):
            s = 0
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == mat[i][c]:
                        s += mat[i][j]  
            if s == 1:
                return True
            else:
                return False                      
       
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row(i) and col(j):
                    count += 1
                    
        return count            
        
