import sys
"""
Tree - (won't work)
- 1
(_,_)   (_,5)  (1,_) (1,5) 


taget=4
coins = 1,3

DP initial = [0,inf,inf, inf, inf]  


DP initial = [0,1,inf, inf, inf]  after c=1


Dp[i] holds min(number coints that sum to i)

program populates array:

(1) starting i =1 for each i
    (2) for each coin c:
        2.1 remain = i - c
        2.2 if remain > 0:
            if dp[remain] is not inf:
                # new way of making value i
                 #store in dp
                Dp[i] = min(dp[i],1+dp[remain]]

final answer in Dp[-1] or dp[-1] = inf if not possible

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [sys.maxint] * amount
        
        for i in range(1,amount+1):
            for c in coins:
                remain = i - c
                if remain > 0:
                    remainCoinsCount = dp[remain]
                    if remainCoinsCount!= sys.maxint:
                        dp[i] = min(dp[i], remainCoinsCount + 1)
                        
        return dp[-1] if dp[-1] is not sys.maxint else -1
    
            
































        
        
        
        
        
        
        
        
        
        
































class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        
        dp = [0] + [math.inf] * amount
        for amt in range(1,amount+1):
            for c in coins:
                remain = amt - c
                if remain >= 0:
                    priorCount = dp[remain]
                    if priorCount is not None:
                        dp[amt] = min(priorCount+1, dp[amt])
        
        return -1 if dp[-1] ==  math.inf else dp[-1]

import math
from functools import cache
class SolutionFarToooSlow:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = list(reversed(sorted(coins)))
        n = len(coins)
        if amount == 0:
            return 0

        @cache
        def dfs(amt, coins, used):
            if amt == 0:
                 return used
            if amt < 0:
                return None
            if not coins:
                return None
            c = coins[0]
            newUsed = used
            newUsed += 1
            remain = amt - c
            
            results = []
            if remain == 0:
                results.append(newUsed)
            if remain > 0:
                if applyAgain := dfs(remain,coins,newUsed):
                    results.append(applyAgain)
                if tryNextCoin := dfs(remain,tuple(coins[1:]),newUsed):
                    results.append(tryNextCoin)
            results.append(dfs(amt,tuple(coins[1:]),used))
            if results := [r for r in results if r]:
                return min(results)
                
        if res := dfs(amount,tuple(coins),0):
            return res
        return -1




class SolutionTooSlow:
    def coinChange(self, coins: List[int], amount: int) -> int:

        added = set()
        if amount == 0:
            return 0

        if any([c for c in coins if c == amount]):
            return 1
        minCoins = math.inf
        toSearch = [[c] for c in coins]

        while toSearch:
            combo = toSearch.pop()
            for c in coins:
                newCombo = list(combo)[:] + [c]
                s = sum(newCombo)
                if s == amount:
                    minCoins = min(minCoins,(len(newCombo)))
                elif s < amount:
                    newCombo = tuple(sorted(newCombo))
                    if newCombo not in added:
                        added.add(newCombo)
                        toSearch.append(newCombo)
        
        return -1 if minCoins == math.inf else minCoins


class SolutionDP:
    def coinChange(self, coins: List[int], amount: int) -> int:

        res = [0] + ([math.inf] * (amount))
        for i in range(amount+1):
            for c in coins:
                priorI = i - c
                if priorI > -1:
                    res[i] = min(res[i], res[priorI] + 1)

        return -1 if res[-1] == math.inf else res[-1]