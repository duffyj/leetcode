class SolutionMessedUp:
    def lengthOfLIS(self, nums):
        n = len(nums)
        res = [1] * (n+1)
        j = n -2
        while j >= 0:
            for i in range(j,n):
                if nums[i] < nums[j]:
                    res[i] = max(res[i],res[i]+1)
            j -= 1
        return max(res)
    
    
class SolutionDP:
    def lengthOfLIS(self, nums):#
        n = len(nums)
        lis = [1] * n   # smallest sequence at each point is 1

        for i in range(n-1,-1,-1): # work backwards updating lis
            for j in range(i,n): # for each val work forward looking for next value in sequence starting at i
                if nums[i] < nums[j]: # we haveteh next number aster nums[i]
                    lis[i] = max(lis[i],lis[j]+1) # sequence length at [i]
        return max(lis)
    
    
class Solution:
    def lengthOfLIS(self, nums):#
        res = [nums[0]]

        for i in nums[1:]:
            if i > res[-1]:
                res.append(i)
            else:
                # find first elemnt grater than
                j = 0
                while i > res[j]:
                    j += 1
                res[j] = i
        return len(res)

