class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        buy_at = 101 # minimaze this
        for i in range(n):
            buy_at = min(buy_at, prices[i])
            profit = prices[i] - buy_at
            max_profit = max(max_profit, profit)
        return max_profit