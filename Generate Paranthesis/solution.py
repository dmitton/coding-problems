class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        answers = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                answers.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return answers
