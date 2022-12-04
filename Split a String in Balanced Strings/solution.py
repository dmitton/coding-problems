class Solution:
    def balancedStringSplit(self, s: str) -> int:
        solutions = 0
        numL = 0
        numR = 0
        
        for i in range(len(s)):
            if numL == numR and numL != 0 and numR != 0:
                print(i)
                solutions += 1
                numL = 0
                numR = 0
                if s[i] == 'R':
                    numR += 1
                elif s[i] =='L':
                    numL += 1
            else:
                if s[i] == 'R':
                    numR += 1
                elif s[i] =='L':
                    numL += 1
        if numL == numR and numL != 0 and numR != 0:
            solutions += 1
        return solutions
