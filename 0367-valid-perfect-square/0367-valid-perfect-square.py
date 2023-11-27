class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l <= r:
            m = l + (r-l)//2
            mSq = m ** 2
            if mSq == num:
                return True
            elif mSq > num:
                r = m - 1
            else:
                l = m + 1
        