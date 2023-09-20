class Solution:
    def missingNumberBits(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)+1):
            res ^= i
        for n in nums:
            res ^=n
        return res

    def missingNumber(self, nums: List[int]) -> int:
        # Gauss
        n = len(nums)
        res = n * (n+1) / 2
        for i in nums:
            res -= i
        return int(res)
        
        