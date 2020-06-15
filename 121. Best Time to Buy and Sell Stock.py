class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_P = 0

        for i in range(len(prices) - 1):
            profit = max(prices[i + 1:]) - prices[i]
            if profit > max_P:
                max_P = profit

        return max_P

