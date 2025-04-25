class Solution(object):
    def dominantIndex(self, nums):
        a = sorted(nums)
        max_value = a[-1]
        index = nums.index(max_value)
        if a[-2] * 2 <= a[-1] or len(a) < 2:
            return index
        else:
            return -1     
        
