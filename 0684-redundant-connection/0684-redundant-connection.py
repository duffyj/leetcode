class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) +1
        parent = list(range(n))
        rank = [1] * n

        def find(p):
            while parent[p] != p:
                p = parent[p]
            return p

        def union(v1,v2):
            p1, p2 = find(v1), find(v2)
            r1,r2 = rank[v1], rank[v2]

            if p1 == p2:
                return True
            if r1 >= r2:
                parent[p2] = parent[p1]                
                rank[v1] += r2
            else:
                parent[p1] = parent[p2]                
                rank[r2] += r1
        for ed in edges:
            if union(*ed):
               return ed 
                         


class SolutionMyversion1:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) +1
        parent = list(range(n))
        rank = [1] * n

        for v1,v2 in edges:
            p1, p2 = parent[v1], parent[v2]
            r1,r2 = rank[v1], rank[v2]

            if p1 == p2:
                return v1,v2
            if r1 >= r2:
                rank[v1] = r1 + 1
                parent[v2] = parent[p1]
            else:
                rank[v2] = r2 + 1
                rank[v1] = r1 + 1
                parent[v1] = parent[p2]       


# neother of these work
class SolutionDFS:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for v1,v2 in edges:
            if v1 not in graph:
                graph[v1] = [v2]
            else:
                graph[v1].append(v2)
        
        visited = set()

        redundantEdges = set()

        def dfs(n,path):
            if n in visited:
                return
            visited.add(n)
            cycle = False
            
            for edge in zip(path,path[1:]):
                if cycle or edge[-1] == n:
                    cycle = not cycle
                    redundantEdges.add(tuple(edge))
            if cycle:
                redundantEdges.add([path[-1],n])
            else:
                for node in graph.get(n,[]):
                    dfs(node,path + [n])

        dfs(edges[0][0],[])

        if redundantEdges:
            for edge in reversed(edges):
                if tuple(edge) in redundantEdges:
                    return edge
            



class SolutionBFS:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for v1,v2 in edges:
            if v1 not in graph:
                graph[v1] = [v2]
            else:
                graph[v1].append(v2)
        
        visited = set()
        redundantEdges = set()

        startNode = (edges[0][0],[])
        queue = deque()
        queue.append(startNode)

        while queue:
            n,path = queue.popleft()
            if n in visited:
                return
            visited.add(n)
            cycle = False
            path = path + [n]
            for edge in zip(path,path[1:]):
                if cycle or edge[-1] == n:
                    cycle = not cycle
                    redundantEdges.add(tuple(edge))
            
            for node in graph.get(n,[]):
                queue.append((node,path))            

        if redundantEdges:
            for edge in reversed(edges):
                if tuple(edge) in redundantEdges:
                    return edge
            
			
