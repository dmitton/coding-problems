class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 1
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "-"
            else:
                count += 1
        
        try:
            while True:
                print(nums)
                nums.remove("-")
        except ValueError:
            pass
        return count
