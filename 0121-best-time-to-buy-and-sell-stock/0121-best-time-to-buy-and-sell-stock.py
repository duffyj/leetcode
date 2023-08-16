



from sys import maxsize
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMinimum = sys.maxsize
        maxProfit = 0
        for p in prices:
            maxProfit = max(maxProfit,p-currMinimum)
            currMinimum = min(currMinimum,p)
        return maxProfit






from sys import maxsize
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        minS,maxP  = maxsize, 0
        for s in prices:
            maxP = max(maxP,s-minS)
            minS = min(minS,s)
        return max(maxP,0)