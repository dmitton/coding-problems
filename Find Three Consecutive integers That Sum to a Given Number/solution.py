class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        sumArray = []

        num1 = int((num / 3) -1)
        num2 = int(num / 3)
        num3 = int((num / 3) + 1)
        if num1 == num2 or num1 == num3 or num2 == num3:
            return []

        total = num1 + num2 + num3
        if total != num:
            return []
        sumArray = [num1, num2, num3]
        sumArray = sorted(sumArray)
        return sumArray
