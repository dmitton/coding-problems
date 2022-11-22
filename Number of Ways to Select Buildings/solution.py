class Solution:
    def numberOfWays(self, s: str) -> int:
        numberSolutions = 0
        n01 = 0
        n10 = 0
        n0 = 0
        n1 = 0
        nums = 0
        # create lists for the number of 1s and 0s at a specific index
        for i in range(len(s)):
            if s[i] == '0':
                n0 += 1
                n10 += n1
                nums += n01
            else:
                n1 += 1
                n01 += n0
                nums += n10
        return nums
