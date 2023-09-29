class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        pt = tuple(point)
        self.points[pt] = self.points.get(pt,0) + 1

    def count(self, point: List[int]) -> int:
        count = 0
        pt = tuple(point)
        adjustments = [(1,1),(-1,-1),(-1,1),(1,-1)]
        for adjI, adjJ in adjustments:
            i= pt[0] + adjI
            j= pt[1] + adjJ
            while i >= 0 and j >=0 and i <= 1000 and j <=1000:
                if diagCorner := self.points.get((i,j)):
                    corner1 = self.points.get((i,pt[1]))
                    corner2 = self.points.get((pt[0],j))
                    if corner1 and corner2:
                        count += 1 * diagCorner * corner1 *corner2

                i+= adjI
                j+= adjJ                       
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)