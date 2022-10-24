class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        
        numDict = {}
        
        count = 1
        
        for i in range(len(nums)):
            numDict[nums[i]] = False
        
        for i in range(size):
            if numDict[nums[i]] == False:
                numDict[nums[i]] = True
                count += 1
            else:
                nums[i] = "-"
        
        try:
            while True:
                nums.remove("-")
        except ValueError:
            pass
        return count
