class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)
    
        expected = set(range(1, n + 1))
        
        for i in range(n):
            row_set = set(matrix[i])  
            if row_set != expected:   
                return False
        
        for j in range(n):
            col_set = set()
            for i in range(n):
                col_set.add(matrix[i][j])
            if col_set != expected:
                return False
        
        return True
