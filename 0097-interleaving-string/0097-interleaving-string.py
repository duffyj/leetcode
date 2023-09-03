


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        dp = [([False] * (l2+1)) for _ in range(l1+1)]
        dp[l1][l2] = True

        for i in range(l1,-1,-1):
            for j in range(l2,-1,-1):
                if ((i < l1 and s1[i] == s3[i+j] and dp[i+1][j]) or
                   ((j < l2 and s2[j] == s3[i+j] and dp[i][j+1]))):
                   dp[i][j] = True
        
        return dp[0][0]
            

from functools import cache
class SolutionDfs:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        cache = {}
        def dfs(i,j):
            
            if i >= l1 and j >= l2:
                return True
            key = i,j
            if key in cache:
                return cache[key]
            
            if ((i < l1 and s1[i] == s3[i+j] and dfs(i+1,j)) or
               (j < l2 and s2[j] == s3[i+j] and dfs(i,j+1))):
               return True
            
            cache[key] = False
            return False

        return dfs(0,0)


class SolutionCrap:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        i,j,k = len(s1)-1,len(s2)-1,len(s3)-1
        while True:
            if i == -1 and j == -1 and k == -1:
                return True
            if j >= 0 and s2[j] == s3[k]:
                j -=1
                k -=1
                continue                
            if i >= 0 and s1[i] == s3[k]:
                i -=1
                k -=1
                continue
            return False
        
     

from functools import cache
class SolutionDFS:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        if all( not len(x)  for x in (s1,s2,s3)):
            return True
        if s1 == s3:
            return not s2
        if s2 == s3:
            return not s1
        if any(not len(x)  for x in (s1,s2,s3)):
            return False
        @cache
        def dfs(i,j,k):
            if k < 0:
                if i == len(s1)-1 or j == len(s2)-1:
                    return False
                return True
            res = []
            if i >= 0:
                if s1[i] == s3[k]:
                    res.append(dfs(i-1,j,k-1))
                res.append(dfs(i-1,j,k))
            if j >= 0:
                if s2[j] == s3[k]:
                    res.append(dfs(i,j-1,k-1))
                res.append(dfs(i,j-1,k))

            return any(res)

        return dfs(len(s1)-1,len(s2)-1,len(s3)-1)
