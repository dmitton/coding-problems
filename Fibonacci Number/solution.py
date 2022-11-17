class Solution:
    def fib(self, n: int) -> int:
        
        fib = []
        for i in range(n + 1):
            if i == 0:
                fib.append(0)
            elif i == 1:
                fib.append(1)
            else:
                num = fib[i - 1] + fib[i - 2]
                fib.append(num)
        return fib[n]
