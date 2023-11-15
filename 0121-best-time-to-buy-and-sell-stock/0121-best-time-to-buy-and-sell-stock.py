class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if min_price > price:
                min_price = price
            if max_profit < price - min_price:
                max_profit = price - min_price
        return max_profit