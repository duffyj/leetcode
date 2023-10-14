        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l) //2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid -1
            else:
                l = mid+1
        return -1
        


class Solutionold:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r-l) //2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid -1
            else:
                l = mid + 1
        return -1


class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        for i,val in enumerate(nums):
            if target == val:
                return i
            if target < val:
                return -1
        return -1
        
        
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right - left) //2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1
            else:
                left = mid +1
        return -1
        