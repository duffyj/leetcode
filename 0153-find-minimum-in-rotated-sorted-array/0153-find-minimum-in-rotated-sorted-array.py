import sys


class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0 
        r = len(nums) -1
        res = sys.maxsize
        while l < r:

            if nums[l] < nums[r]:
                return min(nums[l],res)
            mid = (l + r) // 2
            if nums[l] > nums[mid]:
                r = mid  # search left
            else:
                l = mid +1  # search rigth
        return min(nums[l],res)

class Solution2:
    def findMin(self, nums: List[int]) -> int:
        
        res = 10000000
        l = 0 
        r = len(nums) -1
        while l <=r:
            if nums[l] < nums[r]:
                res =  min(res,nums[l])
                break
                
            mid = (l + r) //2
            res = min(res,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid -1
        return res
                
class SolutionFirstGood:
    def findMin(self, nums: List[int]) -> int:
        res = sys.maxsize
        l, r = 0,len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                return  min(res,nums[l])
            mid = l + (r-l)//2
            res = min(res,nums[mid])
            if nums[mid] < nums[l]:
                r = mid -1     
            else:    
                l = mid + 1                
        return res
                