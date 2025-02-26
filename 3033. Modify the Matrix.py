class Solution(object):
    def modifiedMatrix(self, matrix):
        
        r = len(matrix)
        c = len(matrix[0])

        def ma(col):
            m = 0
            for i in range(r):
                for j in range(c):
                    m = max(m, matrix[i][col])
            return m        

        answer = [[0] * c for i in range(r)]  
        for i in range(r):
            for j in range(c):
                m = ma(j)
                if matrix[i][j] == -1:
                    answer[i][j] = m  
                else:
                    answer[i][j] = matrix[i][j]
        return answer            
          
