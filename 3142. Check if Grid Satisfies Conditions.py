class Solution(object):
    def satisfiesConditions(self, grid):
        n = len(grid)
        for i in range(n):
            m = len(grid[i])
            for j in range(m-1):
                if grid[i][j] == grid[i][j+1]:
                    return False
        for i in range(n-1):
            m = len(grid[i])
            for j in range(m):
                if grid[i][j] != grid[i+1][j]:
                    return False

        return True            

        
