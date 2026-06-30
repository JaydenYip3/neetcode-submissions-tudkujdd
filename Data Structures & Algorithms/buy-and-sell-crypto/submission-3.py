class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_value = prices[0]

        for i in range(1,len(prices)):
            profit = prices[i] - min_value
            result = max(profit, result)
            min_value = min(min_value, prices[i])
        
        return result

        
