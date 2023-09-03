"""
[1,2]

-1,1
1
n^2 storage?

Tree - dfs
dfs values:
    if none left - does current sum = target?
        if so return 1
    else - pop one values and
    updat current sum with +value and -value and return sum of dfs of each 

111

[-1,1, 1]
1,-1, 1

1,1,-1
-1,1,1
1,-1,1

cache at 1 = {

    (2,1) = 1,1
    (0,1 = -1,1 and 1,-1)

}

-1,1
1,1
"""
from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dfs(i,currSum):
          # BaseCase
          if i > n-1:
            if currSum == target:
              return 1
            return 0

          return dfs(i+1,currSum+nums[i]) + dfs(i+1,currSum-nums[i])

        return dfs(0,0)


class SolutionVer1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        steps  = len(nums)
        cache = {}
        def dfs(currVal, i):
            key = currVal,i
            if key in cache:
                return cache[key]
            if i == steps:
                return 1 if currVal == target else 0
            nextVal = nums[i]
            result =  dfs(currVal+nextVal,i+1) + dfs(currVal-nextVal,i+1)
            cache[key] = result
            print (key)
            return cache[key]
        
        return dfs(0,0)
                
        
           