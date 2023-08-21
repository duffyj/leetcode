
import sys

minsize = -10000000000000000 # WHY

class Solution:
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
