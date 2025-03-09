class Solution(object):
    def luckyNumbers(self, matrix):
        result = []
        rows = len(matrix)
        cols = len(matrix[0]) 
        for i in range(rows):
            minVal = min(matrix[i])
            minCol = matrix[i].index(minVal)

            maxInCol = True
            for j in range(rows):
                if matrix[j][minCol] > minVal:
                    maxInCol = False
                    break

            if maxInCol:
                result.append(minVal)

        return result
        
