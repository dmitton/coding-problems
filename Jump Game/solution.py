class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            print(goal)
            if i + nums[i] >= goal:
                goal = i
            else:
                continue
        if goal == 0:
            return True
        else:
            return False
