class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        
        for i in range(len(words)):
            word = list(words[i])  
            left, right = 0, len(word) - 1
            
            while left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            
            words[i] = "".join(word)
        return " ".join(words)      
        
