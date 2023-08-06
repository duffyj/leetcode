class Solution:

    def numIslands(self, grid: List[List[str]]):    
        res = 0
        rumR = len(grid)
        rumC = len(grid[0])
        result = [1]

        visited =[[False]*rumC for _ in range(rumR)]

        toVisit = deque()
        for rowNum in range(rumR):
            for colNum in range(rumC):
               toVisit.append((rowNum,colNum,None))
        
        def doVisit(r,c,i=None):
            if visited[r][c]:
                return
            visited[r][c] = True
            if grid[r][c] is "0":
                return
            if not i:
                result[0] += 1
                i = result[0]
            for adjRow,adjCol in ((1,0),(0,1),(-1,0),(0,-1)):
                newN, newM = r+adjRow, c+adjCol
                if newN >=0 and newN < rumR and newM >=0 and newM < rumC:
                    toVisit.appendleft((newN,newM,i))
        
        while toVisit:
            r,c,i = toVisit.popleft()
            doVisit(r,c,i)


        return result[0]-1























































    
class Solution2:
    res = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0]) 
 
        toSearch = []
        visited = []
        for _ in range(m):
            visited.append([False] * (n))
        
        def visit(i,j, isNew):
            if not visited[i][j]:
                visited[i][j] = True
                if grid[i][j]  == "1":
                    if isNew:
                        self.res += 1
                    for inci, incj in ([1,0], [-1,0], [0,1], [0,-1]):
                        newi, newj = i + inci, j + incj
                        if (0 <= newi < m) and (0 <= newj < n): 
                            if not visited[newi][newj]:
                                toSearch.append((newi,newj))  
        for i in range(m):
            for j in range(n):
                visit(i,j,True)
                while toSearch:
                    point = toSearch.pop()
                    visit(point[0], point[1],False)

        return self.res
                
        