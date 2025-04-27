class Solution(object):
    def strongPasswordCheckerII(self, password):
        l = len(password)
        hasLower = False
        hasUpper = False
        hasDigit = False
        hasSpecialChar = False
        for i in password:
            if i.islower():
                hasLower = True
            if i.isupper():
                hasUpper = True
            if i.isdigit():
                hasDigit = True
            if i in "!@#$%^&*()-+":
                hasSpecialChar = True
        for i in range(1,l):
            if password[i] == password[i-1]:
                return False

        if l >= 8 and hasLower and hasUpper and hasDigit and hasSpecialChar:
            return True  
        else:
            return False                    

                
        
