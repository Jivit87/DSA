class Solution(object):
    def rowAndMaximumOnes(self, mat):
        n = len(mat)
        index = 0
        maxOne = -1

        for i in range(n):
            count = mat[i].count(1)
            if count > maxOne:
                maxOne = count
                index = i
       
       
        return index, maxOne
    

           
           
        

        
