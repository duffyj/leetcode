class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total, res = 0,0, sys.maxsize
        for r,v in enumerate(nums):
            total += v
            while total >= target:
                res = min(res,r-l+1)
                total -=nums[l]
                l += 1
        return 0 if res == sys.maxsize else res


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total, res = 0,0, sys.maxsize
        for r,v in enumerate(nums):
            total += v
            while total - nums[l] >= target:
                total -=nums[l]
                l += 1
            if total >= target: 
                res = min(res,r-l+1)
        return 0 if res == sys.maxsize else res

