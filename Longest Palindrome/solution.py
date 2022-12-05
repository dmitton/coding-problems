class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        wordDict = {}
        for character in s:
            if character in wordDict:
                wordDict[character] += 1
            else:
                wordDict[character] = 1
        print(wordDict)
        size = 0
        maxSize = 0
        for key in wordDict:
            if wordDict[key] % 2 == 0:
                size += wordDict[key]
            else:
                size += (wordDict[key] - 1)
                if wordDict[key] > maxSize:
                    maxSize = wordDict[key]
        if maxSize > 0:
            size += 1
        return size
