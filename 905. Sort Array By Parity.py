class Solution(object):
    def sortArrayByParity(self, nums):
        n = len(nums)
        left = []
        right = []
        i = 0
        while i < n:
            if nums[i] % 2 == 0:
                left.append(nums[i])
            else:
                right.append(nums[i]) 
            i += 1      
        return left + right         
        
