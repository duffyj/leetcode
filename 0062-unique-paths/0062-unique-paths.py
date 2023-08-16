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
