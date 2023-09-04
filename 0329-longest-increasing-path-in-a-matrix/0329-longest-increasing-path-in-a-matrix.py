class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nR = len(matrix)
        nC = len(matrix[0])

        adjustents = [[0,1],[0,-1],[-1,0],[1,0]]
        cache = {}
        def dfs(r,c):
            key = r,c
            if cachedRes := cache.get(key):
                return cachedRes          
            adjDepth = 0
            for adjR, adjC in adjustents:
                newR = r + adjR
                newC = c + adjC
                if newR >=0 and newR < nR and \
                newC >=0 and newC < nC and \
                matrix[r][c] < matrix[newR][newC]:
                    adjDepth = max(adjDepth,dfs(newR,newC))
            result = 1+adjDepth
            cache[key] = result
            return result

        return max(dfs(r,c) for r in range(nR) for c in range(nC))