class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        string1 = ""
        for i in range(len(s)):
            if not s[i].isalnum():
                continue
            elif s[i].isupper():
                string1 += s[i].lower()
            else:
                string1 += s[i]
        if len(string1) == 0:
            return True
        counter1 = 0
        counter2 = len(string1) - 1 
        if len(string1) % 2 == 0:
            while counter1 < counter2:
                if string1[counter1] == string1[counter2]:
                    counter1 += 1
                    counter2 -= 1
                else:
                    return False
        else:
            while counter1 != counter2:
                if string1[counter1] == string1[counter2]:
                    counter1 += 1
                    counter2 -= 1
                
                else:
                    return False
            
        
        return True
