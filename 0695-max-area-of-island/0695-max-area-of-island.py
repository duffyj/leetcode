class Solution:
    def maxAreaOfIsland(self, grid):
        numR = len(grid)
        numC = len(grid[0])
        visited = [[False] * numC for _ in range(numR)]

        adjustments = [(1,0),(-1,0),(0,1),(0,-1)]
        def visit(r,c):
            if r < 0 or r >= numR or c < 0 or c >= numC or visited[r][c] or grid[r][c] == 0:
                return 0        
            visited[r][c] = True
            return 1 + sum([visit(r+rAdj,c+cAdj) for rAdj,cAdj in adjustments])
        
        return max([visit(r,c) for r in range(numR) for c in range(numC)])





























































class SolutionOld:
    def maxAreaOfIsland(self, grid):




        maxx = len(grid[0])
        maxy = len(grid)
        seen = set()
        
        def area(x,y):
            if not (0 <= y < maxy  and 0 <=  x < maxx and grid[y][x] and (x,y) not in seen):
                return 0
            seen.add((x,y))

            return 1 + area(x,y-1) + area(x,y+1) + area(x-1,y) + area(x+1,y)

        return max([area(x,y) for x in range(maxx) for y in range(maxy)])

        
        
        
        