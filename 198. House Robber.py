class Solution(object):
    def rob(self, nums):
        memo = {}
        def helper(idx):
            if idx >= len(nums):
                return 0
            if idx in memo:
                return memo[idx]    
            rob = nums[idx] + helper(idx+2)
            noRob = helper(idx + 1)
            memo[idx] = max(rob, noRob)
            return memo[idx]
        return helper(0)
        
