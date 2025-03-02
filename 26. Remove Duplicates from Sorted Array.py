class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        l = 0
        for r in range(1, n):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]  
        return l + 1        

        
