class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        total = 0 
        res = 0
        nums.sort()
        n = len(nums)
        while r < n:
            total += nums[r]
            while (nums[r] * (r-l+1)) > total + k:
                total -= nums[l]
                l += 1    
            res = max(r-l+1,res)
            r += 1
        return res  


class SolutionCrap:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        total = 0 
        res = 0
        nums.sort()
        n = len(nums)
        while l < n:
            if ((nums[r] * (r-l + 1)) <= total + k) and r < n-1:
                res = max(r-l,res)
                r +=1
                total += nums[r]
            else:
                total -= nums[l]
                l += 1
        return res  