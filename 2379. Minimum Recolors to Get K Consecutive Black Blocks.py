class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        minCol = float("inf")
        for i in range(n - k + 1):
            r = blocks[i:i+k].count("W") 
            minCol = min(r, minCol)
        return minCol    

        
