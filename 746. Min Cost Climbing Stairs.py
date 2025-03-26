class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {}
        def helper(idx):
            if idx >= n:
                return 0
            if idx in memo:
                return memo[idx]    
            one = cost[idx] + helper(idx + 1) 
            two = cost[idx] + helper(idx + 2) 
            memo[idx] = min(one, two)
            return memo[idx]    

        return min(helper(0), helper(1))
        
        
