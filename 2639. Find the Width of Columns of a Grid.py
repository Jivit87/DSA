class Solution(object):
    def findColumnWidth(self, grid):
        m = len(grid)
        n = len(grid[0])
        arr = []
        
        def colMax(c):
            maxLen = 0
            for i in range(m):  
                r = str(grid[i][c])
                maxLen = max(maxLen, len(r))
            return maxLen 
        
        for j in range(n): 
            arr.append(colMax(j))
        
        return arr
