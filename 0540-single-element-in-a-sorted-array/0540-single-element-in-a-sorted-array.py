class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0,n -1
        while l <=r:
            m = l + (r-l)//2
            
            if (m - 1 < 0 or nums[m-1] != nums[m]) and \
               (m + 1 == n or  nums[m+1] != nums[m]):
               return nums[m]
            leftSide = m if nums[m] != nums[m-1] else m -1
            if leftSide % 2:
                r = m - 1
            else:
                l = m + 1               





class SolutionOne:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0,n -1
        while l <=r:
            m = l + (r-l)//2
            
            if m < n -1 and  m > 0 and nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            if (m == 0 and nums[0] != nums[1]) or m == n-1 and nums[m] != nums[m-1]:
                return nums[m]
 
            if nums[m] == nums[m-1]:
                if m % 2:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if m % 2:
                    r = m - 1
                else:
                    l = m + 1               

