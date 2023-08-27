class Solution:
    def climbStairs(self, n: int) -> int:
        priorCounts=[1,1]
        for _ in range(n-1):
            newCount = sum(priorCounts)
            priorCounts = [priorCounts[1], newCount]
        return priorCounts[1]











class SolutionSlow:
    def climbStairs(self, n: int) -> int:
        final = 0
        comb = [1,2]
        while True:
            next = []
            for c in comb:
                if c == n:
                    final += 1
                elif c < n:
                    next.append(c)
            if not next:
                return final
            comb = [nx + 1 for nx in next] + [nx + 2 for nx in next]
            
            
class Solution2:
    def climbStairs(self, n: int) -> int:
        arr = [1,1]
        for _ in range(n -1):
            arr1 = sum(arr)
            arr[0], arr[1] = arr1, arr[0] 
        return arr[0]
            
class SolutionRetyr:
    def climbStairs(self, n: int) -> int:
        arr = [1,1]
        for _ in range(n -1):
            arr1 = sum(arr)
            arr = [arr[1], arr1] 
        return arr[1]
            