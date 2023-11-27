class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l + (r-l) //2
            v = nums[m]
            if v == target:
                return m
            if target < v:  # 6 got n
                r = m - 1
            else:
                l = m +1
        return l





















class Solution2:
    def searchInsert(self, nums, target):
        left  = 0
        right = len(nums) -1
        while left <= right:
           mid = (left + right) // 2
           if  nums[mid] == target:
             return mid
           if target < nums[mid]:
                right = mid - 1
           else:
                left = mid + 1
        return left

class Solution1:
    def searchInsert(self, nums, target):
        lo  = 0
        hi = len(nums) 
        while lo < hi:
           mid = lo + (hi - lo) // 2
           if  nums[mid] == target:
             return mid
           if target <= nums[mid]:
                hi = mid 
           else:
                lo = mid + 1
        return lo
            