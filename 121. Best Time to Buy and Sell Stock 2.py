class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_P = 0
        low = 999999
        for price in prices:
            if price > low:
                profit = price - low
                if profit > max_P:
                    max_P = profit
            else:
                low = price

        return max_P

