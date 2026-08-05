class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy, sell = 0, 1
        maxProfit: int = 0
        while sell < len(prices):
            profit: int = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, profit)
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return maxProfit