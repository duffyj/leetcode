class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nR = len(matrix)
        nC = len(matrix[0])

        zeroRows = set()
        zeroCols = set()
        for r in range(nR):
            for c in range(nC):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)
        
        for zr in zeroRows:
            for i in range(nC):
                matrix[zr][i] = 0
        for zc in zeroCols:
            for i in range(nR):
                matrix[i][zc] = 0                

        