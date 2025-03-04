class Solution(object):
    def sortEvenOdd(self, nums):
        n = len(nums)
        even = [nums[i] for i in range(0, n, 2)] 
        odd = [nums[i] for i in range(1, n, 2)]  
    
        even.sort()
        odd.sort(reverse=True)
        
        result = [0] * n
        e = 0  
        o = 0   
        
        for i in range(n):
            if i % 2 == 0:
                result[i] = even[e]
                e += 1
            else:
                result[i] = odd[o]
                o += 1
        return result
