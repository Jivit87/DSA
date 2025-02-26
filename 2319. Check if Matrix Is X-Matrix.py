class Solution(object):
    def checkXMatrix(self, grid):
        n = len(grid)
        condition = 0
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False        
        return True




        
