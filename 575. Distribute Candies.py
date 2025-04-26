class Solution(object):
    def distributeCandies(self, candyType):
        a = len(candyType) / 2
        s = set(candyType)
        d = len(s)
        return min(a, d)
        
