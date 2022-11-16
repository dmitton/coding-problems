class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        newList = [None] * (len(nums) + 1)
        
        for num in nums:
            newList[num] = num
        
        answer = 0
        for i in range(len(newList)):
            if newList[i] == None:
                answer = i
        
        return answer
