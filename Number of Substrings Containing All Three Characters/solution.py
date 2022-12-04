class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        solutions = 0
        
        for i in range(len(s)):
            newString = s[i:]
            a = newString.find('a')
            b = newString.find('b')
            c = newString.find('c')
            if a == -1 or b == -1 or c == -1:
                continue
            else:
                a = a + i
                b = b + i
                c = c + i
                maxIndex = max(a, b, c)
                solutions += (len(s) - maxIndex)
                
                    
        
        return solutions
