
class Solution:
    def rob(self, nums: List[int]) -> int:
        swag = [0,0]
        for n in nums:
            swag = [swag[1], max(swag[0] + n,swag[1])]
        return max(swag)


#class Solution2:
#    def rob(self, nums: List[int]) -> int:
#        if len(nums) == 1:
#            return nums[0]
#        arr = [nums[0],nums[1]]
#        for i in range(2,len(nums)):
#            val = max(arr[0] + nums[i],arr[1])
#            arr = max(arr), val
#        return max(arr)

import functools
  
class SolutionRecurse:

    def rob(self, nums: List[int]) -> int:
        @functools.cache
        def doRob(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + doRob(i+2), doRob(i+1))
        return doRob(0)

class SolutionDp:
    def rob(self, nums: List[int]) -> int:
        prevprev,  prev = 0, 0
        for v in nums:
            newmax = max(v + prevprev,prev)
            prevprev = prev
            prev = newmax
        return max(prev,prevprev)


class SolutionSmall:
    def rob(self, nums: List[int]) -> int:
        prior = (0, 0)
        for v in nums:
            prior  = (max(v + prior[1],prior[0]), prior[0])
        return max(prior)


class SolutionOrig:
    def rob(self, nums: List[int]) -> int:
        def doRob(subNums):
            if len(subNums) == 1:
                return nums[0]
            arr = [subNums[0],subNums[1]]
            for i in range(2,len(subNums)):
                val = max(arr[0] + nums[i], arr[1])
                arr = [max(arr),val]
            return max(arr)
        return doRob(nums)



    
    
#class Solution2:
#    def rob(self, nums: List[int]) -> int:
#        t1 = 0
#        t2 = 0
#        for current in nums:
#            temp = t1
#            t1 = max(current + t2, t1)
#            t2 = temp
#
#       return t1
        
        