


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        A=0
        B=-100000000000000
        for p in prices:
            A = max(A,B+p)
            B = max(B,-p)
        return A

class SolutionTre2:
    def maxProfit(self, prices: List[int]) -> int:
        t = [[0,0][:] for _ in range(len(prices))] # Sell,Buy Case
        for (p,i) in zip(prices,range(1,len(prices))):
            print(i)
            t[i][0] = max(t[i-1][0],t[i-1][1]-p)
            if i > 1:
                t[i][1] = max(t[i-1][1],t[i-1][0]+p)
        return max(t[-1])
        
        
        
        
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        minS, maxP = prices[0], 0
        for p in prices:
            maxP = max(maxP,p - minS)
            minS = min(minS, p)
        return maxP

from sys import maxsize
class SolutioOrifn:
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