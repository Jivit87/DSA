class Solution(object):
    def findSpecialInteger(self, arr):
        l = len(arr)
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1     
        for key,val in d.items():
            if val > l/4:
                return key  
        return -1         
        
