class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res =0
        modVal = 10**9 + 7
        r = len(nums) -1
        for l,v in enumerate(nums):
            while (v + nums[r]) > target and l <= r:
                r -=1
            if l > r:
                break
            res += 2 ** (r-l)
        return res % modVal
        