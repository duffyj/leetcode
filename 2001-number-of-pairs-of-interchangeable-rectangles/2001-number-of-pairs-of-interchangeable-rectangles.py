class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        res = 0
        for w,h in rectangles:
            r = w/h
            res += ratios.get(r,0)
            ratios[r] = ratios.get(r,0) +1
        return res




        