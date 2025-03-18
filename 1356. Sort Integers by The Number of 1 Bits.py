class Solution(object):
    def sortByBits(self, arr):
        nums = []
        for i in range(len(arr)):
            b = bin(arr[i])
            c = b[2:].count("1")
            nums.append([c,arr[i]])

        nums.sort()
        l = []
        for i in range(len(nums)):
            l.append(nums[i][1])
        return l    
        
