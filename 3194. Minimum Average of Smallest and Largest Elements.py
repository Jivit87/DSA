class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        minAvg = float("inf")
        arr = []
        while l < r:
            avg = (nums[l] + nums[r]) / 2.0
            arr.append(avg)
            minAvg = min(minAvg, avg)
            
            l += 1
            r -= 1
        return minAvg  
        
