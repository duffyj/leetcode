# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l <=r:
            m = l + (r-l) //2
            v = guess(m)
            if v == 0:
                return m
            if v == 1:
                l = m +1
            else:
                r = m -1
        return l

















































    def guessNumber1(self, n: int) -> int:
        l = 0
        r = n +1
        while l <=r:
            mid = l + (r-l) //2
            res = guess(mid)
            if res == 0:
                return mid
            if res  == -1:
                r = mid -1
            else:
                l = mid + 1