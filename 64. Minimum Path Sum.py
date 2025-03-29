class Solution(object):
    def minPathSum(self, grid, i=0, j=0, memo=None):
        if memo is None:
            memo = {}

        if (i, j) in memo:
            return memo[(i, j)]

        if i >= len(grid) or j >= len(grid[0]):
            return float('inf')    

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]  

        memo[(i, j)] = grid[i][j] + min(
            self.minPathSum(grid, i+1, j, memo),
            self.minPathSum(grid, i, j+1, memo)
        )

        return memo[(i, j)]
