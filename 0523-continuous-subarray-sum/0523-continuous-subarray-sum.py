class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:-1}
        total = 0
        for i,n in enumerate(nums):
            total += n
            remian = total % k
            if remian not in seen:
                seen[remian]  = i            
            elif (i - seen[remian]) > 1:
                return True
            