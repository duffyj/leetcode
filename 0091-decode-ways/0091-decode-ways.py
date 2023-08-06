class Solution3:
    def numDecodings(self, s: str) -> int:  
        def isLetter(b2,b1):
            return s[b2] in "012" and s[b1] in "123456"
        backOne,backTwo = 1,1
        for i in range(len(s)-1,-1,-1):
            newCurr = backOne if s[i] != "0" else 0
            if (i < len(s) -1) and isLetter(i,i+1):
                newCurr += backTwo
            backTwo, backOne = backOne, newCurr
        return backOne

class Solution:
    def numDecodings(self, s: str) -> int:  
        dp = {len(s) : 1}
        def isLetter(b2,b1):
            if b2 in "12":
                val = ((int(b2)) * 10 + int(b1)) 
                return val > 0 and val  <= 26

        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i]  = 0
            else:
                dp[i] = dp[i+1]
            if (i < len(s) -1) and isLetter(s[i],s[i+1]):
                dp[i] += dp[i+2]
        return dp[0]


class SolutionDp:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def isLetter(b2,b1):
            val = ((int(b2) or 0) * 10 + int(b1)) 
            return 1 if val > 0 and val  <= 26 else 0 

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if (i + 1) < len(s) and isLetter(s[i],s[i+1]):
                res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)


class SolutionsinglePassOfLiost:
    def numDecodings(self, s: str) -> int:
                
        if s[0] == '0':
            return 0        
        if len(s) in [0,1]:
            return len(s)
        def isLetter(b2,b1):
            val = ((int(b2) or 0) * 10 + int(b1)) 
            return 1 if val > 0 and val  <= 26 else 0 

        res = [0] * len(s)
        for i in range(1,len(s)):
            if res[i-1] > 0:
                continue
            if isLetter(s[i-1],s[i]) and not (res[-1]):
                res[i] = 1
        
        return sum(res)+1


class SolutionTree:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0        
        if len(s) in [0,1]:
            return len(s)
        def isLetter(b2,b1):
            val = ((int(b2) or 0) * 10 + int(b1)) 
            return 1 if val > 0 and val  <= 26 else 0        
        def dfs(i,count):
            if i == len(s):
                return count
            isZero = isLetter(s[i-1],s[i]) if s[i]  != '0' else 0    
            newletterCoding = isLetter(s[i-1],s[i]) if i > 1 else isZero 
            return max(dfs(i+1,count), dfs(i+1,count + newletterCoding))

        return dfs(1,0) +1
class SolutionBestSoFar:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0            
        if len(s) in [0,1]:
            return len(s)
        
        def isLetter(b2,b1):
            val = ((int(b2) or 0) * 10 + int(b1)) 
            return 1 if val > 0 and val  <= 26 else 0       
        back2, back1 = 1, 1
        for i in range(1,len(s)):
            tmpBack1 =  back1
            back1 =  max(back2+isLetter(s[i-1],s[i]),back1) 
            back2 =  tmpBack1
        return  back1            



class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = [0 if s[0] == '0' else 1] + [0] * (n -1)
        for i in range(1,n):

            if s[i] != '0': 
                res[i] += res[i-1] # new digit as sinle value
            if s[i] != '0' or s[i-1] != '0':
                if (int(s[i-1]) * 10)+ int(s[i]) <= 26:
                    res[i] += max(1,res[i-1]-1) # new digity as double numer

        return res[-1] 



class SolutionPain:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = [0] * (n+1)
        res[0] = 1
        res[1] = 0 if s[0] == '0' else 1 

        for i in range(2,len(res)):
            if s[i-1] != '0': 
                res[i] += res[i-1] # new digit as sinle value
                
            v =  int(s[i - 2 : i])
            if v >= 10 and v <= 26:
                res[i] += res[i-2]   # new digity as double number

        return res[n] 

class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # Array to store the subproblem results
        dp = [0 for _ in range(n + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1


        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]
                
        return dp[len(s)]

class SolutionGood:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        oneBack, twoBack  = 1,1
        
        for i in range(1,n):
            cur = oneBack if s[i] != '0' else 0
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                cur += twoBack
            oneBack, twoBack = cur, oneBack
        
        return oneBack


class Solutionsol2:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
    
        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current
        
        return one_back