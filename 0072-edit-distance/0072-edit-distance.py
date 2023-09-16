from functools import cache

class SolutionRaw:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        l1,l2 = len(word1)-1, len(word2)-1
        
        @cache
        def diffMin(p1,p2):
            if p1 == l1 and p2 == l2:
                return 0 if word1[p1] == word2[p2] else 1
            if p1 == l1:
                return l2 - p2
            if p2 == l2:
                return l1 - p1
            
            if word1[p1] == word2[p2]:
                return diffMin(p1+1,p2+1)

            diffRemain = (diffMin(p1+1,p2+1),
                          diffMin(p1+1,p2),
                          diffMin(p1,p2+1))
            mind =  min(diffRemain) 
            return mind +1
        
        return diffMin(0,0)



class SolutionCache:
    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        
        insert = self.minDistance(word1, word2[1:])
        delete = self.minDistance(word1[1:], word2)
        replace = self.minDistance(word1[1:], word2[1:])

        return min((insert,delete,replace)) + 1


class SolutionMin:
    def minDistance(self, word1: str, word2: str):
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        l1, l2 = len(word1), len(word2)
        res = [([math.inf] * (l1+1))[:] for _ in range(l2+1)]
        res [0][0] = 0

        for i in range(1,l1+1):
            for j in range(1,l2+1):
                vals = []
                if i > 0:
                    vals.append(res[j][i-1])
                if j > 0:
                    vals.append(res[j-1][i])  
                if i > 0 and j > 0:
                    vals.append(res[j-1][i-1])

                currDiff = 0 if word1[i-1] == word2[j-1] else 1
                res[j][i] = min(vals) +  currDiff

        return res[-1][-1]                      

class SolutionDP:
    def minDistance(self, word1: str, word2: str):
        
        m, n = len(word1), len(word2)
        res = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m + 1):
            res[i][0] = i
        for j in range(n + 1):
            res[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    res[i][j] = res[i-1][j-1]
                else:
                    res[i][j] = 1 + min((res[i-1][j-1],
                                         res[i][j-1],
                                         res[i-1][j]))
        return res[-1][-1]                      



        
class SolutionCache:
    def minDistance(self, word1, word2):
        l1,l2 = len(word1), len(word2)
        if not l1:
            return l2
        if not l2:
            return l1
            
        @cache
        def dfs(p1,p2):
            if p1 == l1 and p2 == l2:
                return 0
            if p1 == l1:
                return l2-p2
            if p2 == l2:
                return l1-p1
            
            if word1[p1] == word2[p2]:
                return dfs(p1+1,p2+1)

            futherOperations = (dfs(p1+1,p2+1),
                                dfs(p1+1,p2),
                                dfs(p1,p2+1))

            return 1 + min(futherOperations)
        return dfs(0,0)

class SolutionMyCache:
    def minDistance(self, word1, word2):
        l1,l2 = len(word1), len(word2)
        if not l1:
            return l2
        if not l2:
            return l1
            
        dp = [[None] * (l2+1) for _ in range(l1+1)]

        def dfs(p1,p2):
            if dp[p1][p2] == None:
                if p1 == l1 and p2 == l2:
                    return 0
                if p1 == l1:
                    return l2-p2
                if p2 == l2:
                    return l1-p1
                
                if word1[p1] == word2[p2]:
                    return dfs(p1+1,p2+1)

                futherOperations = (dfs(p1+1,p2+1),
                                    dfs(p1+1,p2),
                                    dfs(p1,p2+1))

                dp[p1][p2] =  1 + min(futherOperations)
            return dp[p1][p2]
        x = dfs(0,0)
        return x
    
class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        word1 = word1[::-1]
        word2 = word2[::-1]
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                    print((i,j, word1[i - 1], word2[j - 1],'SAME', table[i][j] ))
                else:
                    options = (table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
                    print((i,j, word1[i - 1], word2[j - 1], 'DIFF', table[i][j],options ))
                    table[i][j] = 1 + min(options)
        return table[-1][-1]

class Solution:
    def minDistance(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)

        dp = [[0] * (l2+1) for _ in range(l1+1)]

        for end1 in range(l1):
            dp[end1][-1] = l1 - end1
        for end2 in range(l2):
            dp[-1][end2] = l2 - end2
        
        for c1 in range(l1-1,-1,-1):
            for c2 in range(l2-1,-1,-1):
                if word1[c1] == word2[c2]:
                    dp[c1][c2] = dp[c1+1][c2+1]
                    print((c1,c2, word1[c1], word2[c2],'SAME', dp[c1][c2] ))
                else:
                    options = (dp[c1+1][c2+1],dp[c1+1][c2],dp[c1][c2+1])
                    print((c1,c2, word1[c1], word2[c2],'DIFF', dp[c1][c2],options ))
                    dp[c1][c2] = 1+ min(options)
        return dp[0][0]
                    
"""(1, 1, 'e', 's', 'DIFF', 0, (1, 1, 0))
(1, 2, 'e', 'o', 'DIFF', 0, (2, 1, 1))
(1, 3, 'e', 'r', 'DIFF', 0, (3, 2, 2))
(2, 1, 's', 's', 'SAME', 1)
(2, 2, 's', 'o', 'DIFF', 0, (2, 1, 1)) <-
(2, 3, 's', 'r', 'DIFF', 0, (3, 2, 2))
(3, 1, 'r', 's', 'DIFF', 0, (1, 3, 2))
(3, 2, 'r', 'o', 'DIFF', 0, (2, 2, 1))
(3, 3, 'r', 'r', 'SAME', 2)
(4, 1, 'o', 's', 'DIFF', 0, (2, 4, 3))
(4, 2, 'o', 'o', 'SAME', 2)
(4, 3, 'o', 'r', 'DIFF', 0, (2, 2, 2))
(5, 1, 'h', 's', 'DIFF', 0, (3, 5, 4))
(5, 2, 'h', 'o', 'DIFF', 0, (2, 4, 3))
(5, 3, 'h', 'r', 'DIFF', 0, (3, 3, 2))

(4, 2, 'e', 's', 'DIFF', 0, (0, 1, 1))
(4, 1, 'e', 'o', 'DIFF', 0, (1, 2, 1))
(4, 0, 'e', 'r', 'DIFF', 0, (2, 3, 2))
(3, 2, 's', 's', 'SAME', 0)
(3, 1, 's', 'o', 'DIFF', 0, (1, 2, 0)) <-
(3, 0, 's', 'r', 'DIFF', 0, (2, 3, 1))
(2, 2, 'r', 's', 'DIFF', 0, (2, 0, 3))
(2, 1, 'r', 'o', 'DIFF', 0, (0, 1, 1))
(2, 0, 'r', 'r', 'SAME', 0)
(1, 2, 'o', 's', 'DIFF', 0, (3, 1, 4))
(1, 1, 'o', 'o', 'SAME', 0)
(1, 0, 'o', 'r', 'DIFF', 0, (1, 0, 0))
(0, 2, 'h', 's', 'DIFF', 0, (4, 2, 5))
(0, 1, 'h', 'o', 'DIFF', 0, (2, 0, 3))
(0, 0, 'h', 'r', 'DIFF', 0, (0, 1, 1))

[[0,1,2,3],
[1,0,0,0],
[2,0,0,0],
[3,0,0,0],
[4,0,0,0],
[5,0,0,0]]


[[0,0,0,5],
[0,0,0,4],
[0,0,0,3],
[0,0,Q0Q,2],
[0,0,0,A1A],
[3,2,1,0]]"""

