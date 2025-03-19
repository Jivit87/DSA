class Solution(object):
    def arrangeCoins(self, n):
        count = 0
        sum = 0
        while sum + count + 1 <= n:
            count += 1
            sum += count
        return count    


                     
        
        
        
