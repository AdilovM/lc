class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for sell_price in prices:
            if min_price > sell_price:
                min_price = sell_price
            if max_profit < sell_price - min_price:
                max_profit = sell_price - min_price
        return max_profit
                