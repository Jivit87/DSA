class Solution(object):
    def sortArrayByParityII(self, nums):
        n = len(nums)
        arr = [0] * (n)
        l = 0
        r = 1
        i = 0
        while i < n:
            if nums[i] % 2 == 0:
                arr[l] = nums[i]
                l += 2
            else:
                arr[r] = nums[i]
                r += 2
            i += 1
        return arr        
        
