class Solution:
    def nthUglyNumber(self, n: int) -> int:
        answers = set()
        answers.add(1)
        counter = 1
        answer = 0
        while counter <= n:
            smallest = min(answers)
            answer= smallest
            answers.add(smallest * 2)
            answers.add(smallest * 3)
            answers.add(smallest * 5)
            answers.remove(smallest)
            counter += 1
        return answer
