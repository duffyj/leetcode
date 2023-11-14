class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        total = sum(arr[:k])
        res = 1 if  total / k >= threshold else 0
        r = 0
        for l in range(k,len(arr)):
            total += arr[l]
            total -= arr[r]
            if total / k >= threshold:
               res += 1 
            r+=1

        return res

        