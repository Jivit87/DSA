class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []
        matrix = []
        for i in range(m):
            start = i * n
            end = (i + 1) * n
            row = original[start: end]
            matrix.append(row)
        return matrix        
        
