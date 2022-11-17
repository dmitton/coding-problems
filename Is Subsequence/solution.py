class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        i = 0
        letter = s[i]
        
        for character in t:
            if character == letter:
                if i == len(s) - 1:
                    return True
                else:
                    i = i + 1
                    letter = s[i]
        return False
