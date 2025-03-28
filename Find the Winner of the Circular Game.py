class Solution(object):
    def findTheWinner(self, n, k):
        fri = []
        for i in range(1, n+1):
            fri.append(i)

        currIdx = 0

        while len(fri) > 1:
            currIdx = (currIdx + k - 1) % len(fri)

            fri.pop(currIdx)

        return fri[0] 
            
