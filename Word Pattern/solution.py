class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) > len(pattern) or len(pattern) > len(words):
            return False
        print(words)
        wordDict = {}
        for i in range(len(pattern)):
            if pattern[i] in wordDict:
                continue
            elif words[i] in wordDict.values():
                continue
            else:
                letter = pattern[i]
                wordDict[letter] = words[i]
        print(wordDict)
        for i in range(len(pattern)):
            word = words[i]
            if not pattern[i] in wordDict:
                return False
            if wordDict[pattern[i]] == word:
                continue
            
            else:
                return False
            
        
        return True
