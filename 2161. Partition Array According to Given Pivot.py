class Solution(object):
    def pivotArray(self, nums, pivot):
        n = len(nums)
        left = []
        right = []
        i = 0
        while i < n:
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] > pivot:
                right.append(nums[i])    
            i += 1
        count = nums.count(pivot)    
        mid = [pivot] * count 
        return left + mid + right   
        
        




        
