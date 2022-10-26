class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answers = []
        sum = 0
        for num in nums:
            sum += num
            answers.append(sum)
        return answers
