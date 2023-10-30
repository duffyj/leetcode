class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(1,len(nums)):
            if i % 2:
                # odd
                if nums[i] < nums[i-1]:
                    nums[i] , nums[i-1] = nums[i-1] , nums[i]
            else:
                if nums[i] > nums[i-1]:
                    nums[i] , nums[i-1] = nums[i-1] , nums[i]

class SolutionMegaSlow:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def partition(left,right):
            pivot = right
            right = pivot -1

            while True:
                while nums[left] < nums[pivot]:
                    left +=1
                while nums[right] > nums[pivot]:
                    right -=1
                
                if right <= left:
                    nums[left],nums[pivot] = nums[pivot], nums[left] 
                    return left
                
                nums[left],nums[right] = nums[right], nums[left] 
                left +=1
            
        def quicksort(left,right):
            if left < right:
                pivot = partition(left,right)
                quicksort(left,pivot-1)
                quicksort(pivot+1, right)

        quicksort(0,n-1)
        tmp = nums[:]
        l,r = 0, n-1
        nptr = 0
        while nptr < n:
            nums[nptr] = tmp[l]
            nptr+=1
            l +=1 
            if nptr == n:
                break
            nums[nptr] = tmp[r]
            nptr +=1
            r -=1       


