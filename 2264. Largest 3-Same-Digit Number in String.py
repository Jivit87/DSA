class Solution(object):
    def largestGoodInteger(self, num):
        num = list(num)
        l = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                l.append(num[i]*3)
        if l:
            return max(l)
        else:
            return ""                     
                    
        
