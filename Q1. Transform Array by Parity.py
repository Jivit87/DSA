class Solution(object):
    def transformArray(self, nums):
        arr = []
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                arr.append(1)
            else:
                arr.append(0)
        arr.sort()
        return arr
                
        
