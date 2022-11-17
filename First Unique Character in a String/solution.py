class Solution:
    def firstUniqChar(self, s: str) -> int:
        wordDict = {}
        for letter in s:
            if letter in wordDict:
                wordDict[letter] += 1
            else:
                wordDict[letter] = 1
        
        answer = 0
        for key in wordDict:
            if wordDict[key] == 1:
                answer = s.index(key)
                break
            else:
                answer = -1
        
        return answer
