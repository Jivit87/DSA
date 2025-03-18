class Solution(object):
    def divideArray(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for key, val in d.items():
            if val % 2 != 0:
                return False
        return True                  
        
