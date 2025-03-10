class Solution(object):
    def validStrings(self, n):
        arr = []
        
        for i in range(2 ** n):
            b = bin(i)[2:]  
            b = "0" * (n - len(b)) + b 
            
            if "00" not in b: 
                arr.append(b)
        
        return arr
