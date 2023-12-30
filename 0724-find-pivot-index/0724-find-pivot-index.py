class Solution:
    def pivotIndexComplex(self, nums: List[int]) -> int:
        lenN = len(nums)
        sumLHS = [None] * lenN
        sumRHS = [None] * lenN

        priorL = priorR = 0
        for l,n in enumerate(nums):
            r = lenN - l - 1
            sumLHS[l] = priorL
            sumRHS[r] = priorR
            priorL += nums[l]
            priorR += nums[r]

        for i,(sumL,sumR) in enumerate(zip(sumLHS,sumRHS)):
            if sumL == sumR:
                return i

        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        lhs = 0
        for i, n in enumerate(nums):
            rhs = total - n - lhs
            if lhs == rhs:
                return i
            lhs += n
            
        return -1
            


 