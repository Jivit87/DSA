class Solution(object):
    def maxPower(self, s):
        max = 0
        for i in range(len(s)):
            count = 0
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    count += 1
                if s[i] != s[j]:
                    break
            if count > max:
                max = count   
        return max                 
                    

        
        
