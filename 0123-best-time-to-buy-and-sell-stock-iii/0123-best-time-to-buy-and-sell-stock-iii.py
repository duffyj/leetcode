
import sys

minsize = -10000000000000000 # WHY

class SolutionFormulaNames:
    def maxProfit(self, prices: List[int]) -> int:
            ti10 = 0
            ti20  = 0
            ti11 = minsize
            ti21 = minsize
            for p in prices:
                ti20 = max(ti20,ti21 + p)
                ti21 = max(ti21,ti10 - p)
                ti10 = max(ti10,ti11 + p)
                ti11 = max(ti11,-p)
            return ti20

        
import sys

minsize = -10000000000000000 # WHY

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            afterSell1 = 0
            afterSell2  = 0
            afterBuy1 = minsize
            afterBuy2 = minsize
            for p in prices:
                afterSell2 = max(afterSell2,afterBuy2 + p)
                afterBuy2 = max(afterBuy2,afterSell1 - p)
                afterSell1 = max(afterSell1,afterBuy1 + p)
                afterBuy1 = max(afterBuy1,-p)
            return afterSell2
