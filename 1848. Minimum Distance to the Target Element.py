class Solution(object):
    def getMinDistance(self, nums, target, start):
        minDist = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                minDist= min(minDist, abs(i - start))  
        
        return minDist
        
