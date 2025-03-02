class Solution(object):
    def compress(self, chars):
        l = 0
        r = 0
        while r < len(chars):
            char = chars[r]
            count = 0
            while r < len(chars) and chars[r] == char:
                count += 1
                r += 1
            chars[l] = char    
            l += 1

            if count > 1:
                for i in str(count):
                    chars[l] = i
                    l += 1
            
        return l
