class Solution(object):
    def isToeplitzMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            elem = matrix[i][0]
            for j in range(m):
                if matrix[i][j] != elem:
                    return False
        return True            

        
