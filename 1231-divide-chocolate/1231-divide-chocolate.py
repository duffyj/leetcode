class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def divide(target):
            sum_,count = 0, 0
            for s in sweetness:
                 sum_ += s
                 if sum_ >= target:
                     count += 1
                     sum_  = 0
            return count

        lo, hi = min(sweetness), sum(sweetness)//(k+1)

        while lo < hi:
            mid = (lo + hi +1) //2
            if divide(mid) < k+1:
                hi = mid -1
            else:
                lo = mid
        return lo
