

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, isBuying):
            if i >= len(prices):
                return 0
            if (i,isBuying) in dp:
                return dp[(i,isBuying)]
            
            hold = dfs(i+1, isBuying)
            if isBuying:
                sellTomorrow = dfs(i+1, False)
                dp[(i, isBuying)] = max(hold,sellTomorrow-prices[i])
            else:
                buyTomorrow = dfs(i+2,True)
                dp[(i,isBuying)] = max(hold,buyTomorrow+prices[i])
            return dp[(i, isBuying)]
                
        return dfs(0,True)
            
    
            
BUY = 'B'
SELL = 'S'
HOLD = 'H'
COOL = 'C'
SKIP = 'SK'
         
            
        

class SolutionSlow:
    def maxProfit(self, prices: List[int]) -> int:
        state = [(BUY,-prices[0],),(SKIP,0)]
        state = set(state)
        maxProfit = [0]
        for p in prices[1:]:
            newState = set()
            for action,profit in state:
                def addBuy():
                    newState.add((BUY,profit-p))
                def addSell():
                    maxProfit[0] = max(maxProfit[0],profit+p)
                    if maxProfit[0] == profit+p:
                        newState.add((SELL,profit+p))
                def addHold():
                    newState.add((HOLD,profit))
                if action == BUY:
                    addSell()
                    addHold()
                elif action == SELL:
                    newState.add((COOL,profit))
                elif action == HOLD:
                    addHold()
                    addSell()
                elif action in (COOL,SKIP):
                    addBuy()
                    newState.add((SKIP,profit))
            state = newState
        return max(s[1] for s in state)
 