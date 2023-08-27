class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        for r in range(len(tri)-2,-1,-1):                       
            tri[r] = [tri[r][i] + min(tri[r+1][i],tri[r+1][i+1]) for i in range(len(tri[r]))]    
        return min(tri[0])