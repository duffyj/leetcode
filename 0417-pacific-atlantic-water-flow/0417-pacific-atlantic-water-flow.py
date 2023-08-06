import sys
from itertools import chain
minsize = ~sys.maxsize

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        adjustments = [(1,0), (-1,0), (0,1), (0,-1)]

        numR = len(heights)
        numC = len(heights[0])

        atlanticFlows = set()
        pacificFlows = set()
    
        def visit(r,c, ocean, lastheight = minsize):
            # exit caluse
            curr = (r,c)
            if (
                r < 0 or
                c < 0 or
                r >= numR or
                c >= numC or
                heights[r][c] < lastheight or
                curr in ocean
            ):
                return
            ocean.add(curr)
            for adjR, adjC in adjustments:
                visit(r + adjR, c + adjC, ocean, heights[r][c])
        
        for col in range(numC):
            visit(0,col, pacificFlows)
            visit(numR-1,col, atlanticFlows)
        
        for row in range(numR):
            visit(row, 0, pacificFlows)
            visit(row, numC-1, atlanticFlows)

        return  pacificFlows.intersection(atlanticFlows)           


class SolutionLeetsd:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        return atl.intersection(pac) 

class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        adjustments = [(1,0), (-1,0), (0,1), (0,-1)]

        def unvisited(r,c):
            return [[False] * c for _ in range(r)]

        numR = len(heights)
        numC = len(heights[0])

        atlanticFlows = set()
        pacificFlows = set()
    
        def visit(r,c, flows, lastheight = minsize):
            if heights[r][c] >= lastheight:
                curr = (r,c)
                if not visited[r][c]:
                    visited[r][c] = True
                    flows = flows[:] + [curr]
                    for adjR, adjC in adjustments:
                        newR, newC = r+adjR, c+adjC
                        if newR >= numR or newC >= numC:
                            atlanticFlows.update(flows)
                        elif newR < 0 or newC < 0:
                            pacificFlows.update(flows)
                        else:
                            visit(newR,newC, flows, heights[r][c])

        
        borders = chain.from_iterable([[(0,col), (numR-1,col)] for col in range(numC)] +
                                      [[(row,0), (row,numC-1)] for row in range(1,numR-1)])
        for r,c in borders:
            visited = unvisited(numR,numC)
            visit(r,c,[])

        return list(atlanticFlows.intersection(pacificFlows))
        
class SolutionOLD:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        adjustments = [(1,0), (-1,0), (0,1), (0,-1)]

        def unvisited(r,c):
            return [[False] * c for _ in range(r)]

        numR = len(heights)
        numC = len(heights[0])

        visited = unvisited(numR,numC)

        atlanticFlows = set()
        pacificFlows = set()
        
        def addflows(flows,ocean):
            for f in flows:
                ocean.add(f)

        def visit(r,c, flows, lastheight = 1000000):
            if heights[r][c] <= lastheight:
                curr = (r,c)
         
                if not visited[r][c]:
                    visited[r][c] = True
                    flows = flows[:] + [curr]
                    for adjR, adjC in adjustments:
                        newR, newC = r+adjR, c+adjC
                        if newR >= numR or newC >= numC:
                            addflows(flows,atlanticFlows)
                        elif newR < 0 or newC < 0:
                            addflows(flows,pacificFlows)
                        else:
                            visit(newR,newC, flows, heights[r][c])

        for r in range(numR):
            for c in range(numC):
                visited = unvisited(numR,numC)
                if (r,c) == (1,2):
                    print(1)
                visit(r,c,[])

        res = list(atlanticFlows.intersection(pacificFlows))
        res.sort()
        return res




class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        adjustments = [(1,0), (-1,0), (0,1), (0,-1)]

        def unvisited(r,c):
            return [[False] * c for _ in range(r)]

        numR = len(heights)
        numC = len(heights[0])

        visited = unvisited(numR,numC)

        atlanticFlows = set()
        pacificFlows = set()
        
        def addflows(flows,ocean):
            for f in flows:
                ocean.add(f)

        def visit(r,c, flows, lastheight = 1000000):
            if heights[r][c] <= lastheight:
                curr = (r,c)
                if visited[r][c]:
                    if curr in atlanticFlows:
                        addflows(flows,atlanticFlows)
                    if curr in pacificFlows:
                        addflows(flows,pacificFlows)
                else:
                    visited[r][c] = True
                    flows = flows[:] + [curr]
                    for adjR, adjC in adjustments:
                        newR, newC = r+adjR, c+adjC
                        if newR >= numR or newC >= numC:
                            addflows(flows,atlanticFlows)
                        elif newR < 0 or newC < 0:
                            addflows(flows,pacificFlows)
                        else:
                            visit(newR,newC, flows, heights[r][c])

        for r in range(numR):
            for c in range(numC):
                visited = unvisited(numR,numC)
                if (r,c) == (1,2):
                    print(1)
                visit(r,c,[])

        res = list(atlanticFlows.intersection(pacificFlows))
        res.sort()
        return res


