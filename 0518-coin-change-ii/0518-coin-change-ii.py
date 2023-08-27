class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        numC = len(coins)
        if numC == 0:
            return 0
        if amount == 0:
            return 1
        res = []
        row = [1]+ ([0] * amount)
        for _ in range(numC):
            res.append(row[:])
        
        for i in range(numC-1,-1,-1):
            for a in range(1,amount+1):
                remain = a - coins[i]
                if remain >= 0:
                    res[i][a] += res[i][remain]
                if i < numC-1:
                    res[i][a] += res[i+1][a]
        return res[0][-1]


class SolutionLeeet:
    def change(self, amount: int, coins: List[int]) -> int:
        # MEMOIZATION
        # Time: O(n*m)
        # Memory: O(n*m)
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]
        return dfs(0, 0)

class SolutionMyCache:
    def change(self, amount: int, coins: List[int]) -> int:
      cache = {}

      def dfs(i,a):
        key = (i,a)
        if a == amount:
          return 1
        if a > amount or i == len(coins):
          return 0
        if key in cache:
          return cache[key]
        cache[key] = dfs(i,a + coins[i]) + dfs(i+1,a)
        return cache[key] 
      return dfs(0,0)

class SolutionTLE:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        arr = [set() for _ in range(amount+1)]
        coins.sort()
        for a in range(1,amount+1):
            for c in coins:
                remain = a - c
                if remain is 0:
                    arr[a].add((c,))
                elif remain > 0:
                    for comb in arr[remain]:
                        newComb = list(comb)
                        newComb.append(c)
                        newComb.sort()
                        arr[a].add(tuple(newComb))

        return len(arr[-1]) if arr[-1] else 0