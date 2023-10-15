class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(B) < len(A):
            A,B = B,A
        
        l,r = 0 ,len(A) -1
        while True:
            m = l + (r-l) //2 # A mid 
            Bm = half - m - 2 # B mid

            AL = A[m] if m >= 0 else float('-inf')
            AR = A[m+1] if  (m+1) < len(A) else float('inf')
            BL = B[Bm] if Bm >= 0 else float('-inf')
            BR = B[Bm+1] if  (Bm+1) < len(B) else float('inf')

            if AL <= BR and BL <= AR:
                # exit case
                return  min(AR,BR) if total % 2 else (min(AR,BR) + max(AL,BL)) / 2
            if AL > BR:
                r = m -1
            else:
                l = m +1
