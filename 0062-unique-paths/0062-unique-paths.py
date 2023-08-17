from functools import cache
class SolutionMomoise:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1
        
        return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)


class Solution:
   def uniquePaths(self, m: int, n: int) -> int:
        arr = [[1] * n for _ in range(m)]

        for row in range(1,m):        
            for col in range(1,n):
                arr[row][col] = arr[row-1][col] + arr[row][col-1]

        return arr[m-1][n-1]

    
class Solutionbad:
    def uniquePaths(self, m: int, n: int):
        paths = [([0] * n)[:] for _ in range(m)]
        paths [m-1][n-1] = 1
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                print((r,c))
                if c < n-1:
                    paths[r][c] += paths[r][c+1]
                if r < m -1:
                    paths[r][c] += paths[r+1][c]
        return paths[0][0]

class Solution:
    def uniquePaths(self, m: int, n: int):
        paths = [([0] * n)[:] for _ in range(m)]
        paths [0][0] = 1
        for r in range(m):
            for c in range(n):
                if c > 0:
                    paths[r][c] += paths[r][c-1]
                if r >0:
                    paths[r][c] += paths[r-1][c]
        return paths[m-1][n-1]