class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1,1
        for n in nums:
            currTmp = currMax * n
            currMax = max(currTmp, currMin*n, n)
            currMin = min(currTmp, currMin*n, n)
            res = max(res,currMax)
        return res

        