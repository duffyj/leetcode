
class SolutionQuickSort:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(L,R):
            P = R
            R = P - 1
            while True:
                while nums[L] < nums[P]:
                    L+=1
                while nums[R] > nums[P]:# and R >= 0:
                    R-=1     
                if L >= R:
                    nums[L],nums[P] = nums[P],nums[L]
                    return L
                nums[L],nums[R] = nums[R],nums[L] 
                L += 1
                
        def quicksort(L,R):
            if R-L <= 0:
                return
            P = partition(L,R)
            quicksort(L,P-1)
            quicksort(P+1,R)

        quicksort(0,len(nums)-1)


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        L = 0
        R = len(nums) -1
        i = 0

        def swap(i,j):
            nums[i],nums[j] = nums[j],nums[i]            
        while i <=R:
            if nums[i] == 0:
                swap(L,i)
                L +=1
            elif nums[i] == 2:
                swap(i,R)
                R -=1
                i -=1
            i +=1

                