class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        n = len(nums)
        if n < 2:
            return 0
        l = 0
        r = 1
        maxDiff = float("-inf")
        while r < n:
            diff = nums[r] - nums[l]
            maxDiff = max(diff, maxDiff) 
            l += 1
            r += 1
        return maxDiff    

        
        
