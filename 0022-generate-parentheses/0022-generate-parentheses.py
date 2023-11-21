class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def backTrace(params, l=0, r=0):
            if l == n and r == n:
                results.append(''.join(params))
                return
            if l < n:
                backTrace(params + ['('], l=l+1, r=r)
            if r < l:
                backTrace(params + [')'], l=l, r=r+1)

        backTrace([])
        return results
                            




    class SolutionOLD:
        def generateParenthesis(self, n: int) -> List[str]:
            res = []
            def backTrace(S,l=0,r=0):
                if len(S) == n * 2:
                    res.append(''.join(S))
                    return
                if l < n:
                    S.append('(')
                    backTrace(S,l+1,r)
                    S.pop()
                if r < l:
                    S.append(')')
                    backTrace(S,l,r+1)
                    S.pop()
                    
            backTrace([])
            return res