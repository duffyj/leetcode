class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.data = []
        for row in matrix:
            total = 0
            self.data.append([])
            for i,v in enumerate(row):
                total +=v
                self.data[-1].append(total + (self.data[-2][i] if len(self.data) >= 2 else 0))

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        bottomRight = self.data[row2][col2]
        topRight = self.data[row1 - 1][col2] if row1 > 0 else 0
        bottomLeft = self.data[row2][col1-1] if col1 > 0 else 0
        topLeft = self.data[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return bottomRight - topRight - bottomLeft + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)