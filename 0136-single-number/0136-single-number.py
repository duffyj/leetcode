
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = xor(res,n)
        return res

class SolutionOld:
    def singleNumber(self, nums: List[int]) -> int:
        val = 0
        for i in nums:
            val = val ^ i
        return val