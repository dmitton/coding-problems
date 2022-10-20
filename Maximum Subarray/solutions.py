class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        index = 0
        size = 0
        longest = nums[index]
        solutions = []
        
        solutions.append(nums[index])
        while not index == len(nums) - 1:
            index += 1
            distance = solutions[index - 1] + nums[index]
            if distance < nums[index]:
                solutions.append(nums[index])
                size = nums[index]
            else:
                if distance > longest:
                    longest = distance
                    size += distance
                    solutions.append(longest)
                else:
                    solutions.append(distance)
        return max(solutions)
