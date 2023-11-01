class Solution:
    def arraySign(self, nums: List[int]) -> int:
        positive = 1
        for n in nums:
            if n == 0:
                return 0
            positive *= (1 if  n > 0 else -1)
        return positive


            