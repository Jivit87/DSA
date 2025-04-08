class Solution(object):
    def numSquares(self, n):
        memo = {}
        def minSquare(remaining):
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            minCount = float('inf')    
            for i in range(1, int(math.sqrt(remaining)) + 1):
                square = i * i
                minCount = min(minCount, 1 + minSquare(remaining - square))   
            memo[remaining] = minCount
            return minCount
        return minSquare(n)                 
        
        
