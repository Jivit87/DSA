class Solution(object):
    def matrixReshape(self, mat, r, c):
        matrix = []
        for i in mat:
            for j in i:
                matrix.append(j)
        result = []
        if len(matrix) != r * c:
            return mat
        for i in range(r):
            start = i * c
            end = (i + 1) * c
            row = matrix[start: end]
            result.append(row)
        return result        

        
