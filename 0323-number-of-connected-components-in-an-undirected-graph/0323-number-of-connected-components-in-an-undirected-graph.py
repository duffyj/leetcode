class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        rank = [1] * n

        def find(p):
            priorP = p
            while par[p] != p:
                p = par[p]
                par[priorP] = p
            return p
        
        def union(v1,v2):
            p1,p2 = find(v1),find(v2)
            par[p2] = p1
            
        def union2(v1,v2):
            p1,p2 = find(v1),find(v2)
            par[p2] = p1
        

        for ed in edges:
            union(*ed)
        
        return len(set((find(p) for p in par)))