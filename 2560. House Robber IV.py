class Solution(object):
    def minCapability(self, nums, k):
        left, right = min(nums), max(nums)
    
        def canRob(mid):
        
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 2 
                else:
                    i += 1
            return count >= k
        
        
        result = right
        while left <= right:
            mid = (left + right) // 2
            if canRob(mid):
                result = mid
                right = mid - 1  
            else:
                left = mid + 1  
        
        return result



        
