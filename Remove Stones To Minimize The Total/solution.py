class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        newPiles = []
        for pile in piles:
            pile = -abs(pile)
            newPiles.append(pile)
        piles = newPiles
        heapq.heapify(piles)
        while k > 0:
            num = heapq.heappop(piles)
            newNum = math.floor(num / 2)
            heapq.heappush(piles, newNum)
            k = k - 1
        piles2 = []
        for pile in piles:
            pile = abs(pile)
            piles2.append(pile)
        return sum(piles2)
        
