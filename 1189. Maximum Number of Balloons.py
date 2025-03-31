class Solution(object):
    def maxNumberOfBalloons(self, text):
        d = {}
        for i in text:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
            
        a = min(d.get("b", 0), d.get("a", 0), d.get("l", 0)//2, d.get("o", 0)//2, d.get("n", 0))
        return a
               

       
            
        
