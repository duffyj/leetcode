"""
Cannot just count nodes becase of cycles
(1) build adjacency list
(2) start dfs searching a node. If graph is tree we will not see the same node again. Do Dfs:
    (2.1) if visited node return false (graph != tree)
    (2.2) add node to visited.
    (2.3) visit current node (appart from the one we just came from)

(3 if all nodes have been visted then graph is a tree

"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjacents = [[] for _ in range(n)]
        
        
        for v1,v2 in edges:
            adjacents[v1].append(v2)
            adjacents[v2].append(v1)

        visited = set()
        
        def dfs(v,prev=None):
            if v in visited:
                return False
            visited.add(v)
            if not all((dfs(a,v) for a in adjacents[v] if a != prev)):
                return False
            return True

        return dfs(0) and len(visited) == n



#=======================================================
        if True:
            head = find(par[0])
            seen = [0] * n
            def dfs(v):
                if seen[v] is 1:
                    return False
                seen[v] +=1
                if adjacents[v]:
                    return all((dfs(adj) for adj in adjacents[v]))
                return True

            if not dfs(find(par[0])):
                return False

            return set(seen) == {1} 

                
        