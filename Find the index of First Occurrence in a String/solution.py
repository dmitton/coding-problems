class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                break;
            if haystack[i] == needle[0]:
                indexH = i
                indexN = 0
                isSame = True
                while indexN < len(needle) and indexH < len(haystack):
                    print(indexH)
                    print(indexN)
                    if haystack[indexH] == needle[indexN]:
                        indexH = indexH + 1
                        indexN = indexN + 1
                    else:
                        isSame = False
                        break
                if isSame == True:
                    return i
        return -1
                
