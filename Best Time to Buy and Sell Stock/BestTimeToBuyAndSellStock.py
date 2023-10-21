class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = float('inf')
        for i in range(len(prices)):
            if (prices[i] < lowest):
                lowest = prices[i]
            if (prices[i] - lowest) > profit:
                profit = prices[i] - lowest
        return profit
                