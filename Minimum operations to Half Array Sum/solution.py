class Solution:
    def halveArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        newArray = []
        for num in nums:
            num =  -abs(num)
            newArray.append(num)
        heapq.heapify(newArray)
        total = sum(newArray)
        target = total / 2
        numTimes = 0
        isHalf = False
        while isHalf == False:
            maxNum = heapq.heappop(newArray)
            maxNum = maxNum / 2
            heapq.heappush(newArray, maxNum)
            total = total - maxNum
            numTimes += 1
            if target <= total:
                isHalf = True
        
        return numTimes
