class Solution:
    def searchRange(self, arr: List[int], val: int) -> List[int]:

        def findIndex(searchLeft=True):
            '''
            arr = [left……..….…mid………………..right]
            arr = [left…….mid-1] mid [mid+1……..right]
            '''
            n = len(arr)
            l,r = 0, n-1
            priorMid = None
            while l <= r:
                mid = l + (r-l)//2
                if arr[mid] == val:
                    priorMid = mid
                    if searchLeft:
                        r = mid -1
                    else:
                        l = mid + 1
                elif arr[mid] < val:
                    # search right
                    l = mid + 1
                else:
                    # search left
                    r = mid -1
            return priorMid
        #def findCount(arr, val):
        l = findIndex()
        if l == None:
            return [-1,-1]
        return [l, findIndex(False)]

"""
# from interview.,io
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findIndex(arr,val, searchLeft=True):
            '''
            arr = [left……..….…mid………………..right]
            arr = [left…….mid-1] mid [mid+1……..right]
            '''
            n = len(arr)
            l,r = 0, n-1
            priorMid = None
            while l <= r:
                mid = l + (r-l)//2
                if arr[mid] == val:
                    priorMid = mid
                    if searchLeft:
                        r = mid -1
                    else:
                        l = mid + 1
                elif arr[mid] < val:
                    # search right
                    l = mid + 1
                else:
                    # search left
                    r = mid -1
            return priorMid
        #def findCount(arr, val):
        l = findIndex(nums,target)
        if l == None:
            return [-1,-1]
        return [l, findIndex(nums,target,False)]
"""


class SolutionBitCrap:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) -1
        foundLower,foundUpper = False,False
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid == 0 or (mid > 0 and nums[mid-1] < target):
                    foundLower = True
                    break
                if mid == n or (mid < n and nums[mid+1] > target):
                    foundUpper = True
                    break
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        if not (foundLower or  foundUpper):
            return [-1,-1]
        
        bound1 = mid
        if foundUpper:
            left = 0
            right = mid-1
        else:
            left = mid
            right = len(nums) -1   
            
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if not foundLower and mid == 0 or (mid > 0 and  nums[mid-1] < target):
                    return [mid,bound1]
                if mid == n or (mid < n and nums[mid+1] > target):
                    return [bound1, mid]
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

class SolutionMine1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(findFirst, lower=None):
            left, right = lower or 0, len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if findFirst:
                        if mid == left or nums[mid-1] < target:
                            return mid
                        right = mid -1
                    else:
                        if mid == right or nums[mid+1] > target:
                            return mid
                        left = mid + 1
                else:
                    if target < nums[mid]:
                        right = mid -1
                    else:
                        left = mid + 1
                        
        lower = search(True)
        if lower is None:
            return [-1,-1]
        
        return [lower,search(False, lower)]
        