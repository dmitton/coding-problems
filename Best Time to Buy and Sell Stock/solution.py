class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 0
        number = prices[0]
        for price in prices:
            if price < number:
                number = price
            else:
                if price - number > lowest:
                    lowest = price - number
        return lowest
