class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res,minDiff = None, sys.maxsize
        for a,b in zip(arr, arr[1:]):
            pairDiff = abs(a-b)
            if pairDiff <= minDiff:
                if pairDiff < minDiff:
                     res = []
                     minDiff = pairDiff
                res.append((a,b))
        return res

class SolutionPythonicSmall:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]  
