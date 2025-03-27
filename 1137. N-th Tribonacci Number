class Solution(object):
    def tribonacci(self, n, memo = {}):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        memo[n] = self.tribonacci(n - 1, memo) + self.tribonacci(n - 2, memo) + self.tribonacci(n - 3, memo)
        return memo[n]
        
