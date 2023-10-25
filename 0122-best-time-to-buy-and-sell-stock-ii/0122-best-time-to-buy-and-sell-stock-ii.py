class SolutionSimpe:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -10000000000000
        profit = 0
        for n in nums:
            buy = max (-p,buy)
            profit = max(n+buy,profit)
        return profit









































































class SolutionSimpe:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range (1,len(prices)):
            if prices[i-1] < prices[i]:
                profit +=  prices[i] - prices[i-1]
        return profit
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, bought = 0, -10000000000000

        for p in prices:
            oldSold = sold
            sold = max(sold,bought+p)
            bought = max(bought,oldSold-p)
        return sold