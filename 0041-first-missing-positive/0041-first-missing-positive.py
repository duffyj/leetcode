class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numN= len(nums)
        if numN == 1:
            return nums[0] + 1 if nums[0] in (0,1) else 1
        whichN = [None] * numN
        for n in nums:
            if n > 0 and n <= numN:
                whichN[n-1] = True
        for i,tf in enumerate(whichN):
            if not tf:
                return i+1
        return numN +1

class SolutionLeet:
    def firstMissingPositive(self, nums: List[int]) -> int:
        A = nums
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0
            
        for i in range(len(A)):
            val = abs(A[i])
            if 1 <= val <= len(A):
                if A[val - 1] > 0:
                    A[val - 1] *= -1
                elif A[val - 1] == 0:
                    A[val - 1] = -1 * (len(A) + 1)
        
        for i in range( 1, len(A)+ 1):
            if A[i -1] >= 0:
                return i
        
        return len(A) + 1
        
    def firstMissingPositive_2(self, nums: List[int]) -> int:
        new = set(nums)
        i = 1
        while i in new:
            i += 1
        return i


class SolutionRubbish:
    def firstMissingPositive(self, nums: List[int]) -> int:
        newNums = set()
        minVal = sys.maxsize
        for _ in range(2):
            for n in nums:
                if n > 0 and n < minVal:
                    newNums.add(n)
                    minVal = min(minVal,n)
            nums = list(newNums)
        return nums[0] -1

class SolutionTmp:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numN= max(len(nums),2)
        whichN = [None] * numN
        whichN[0] = True
        for n in nums:
            if n > 0 and n < numN:
                whichN[n] = True
        for i,tf in enumerate(whichN):
            if not tf:
                return i
        return numN
