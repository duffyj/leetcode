"""
[[1,0] [1,2] , [1,3]] = take 3,2,0 and then 1
[[1,0] [1,2] , [1,3], [1,1]] = take not possible

1. loop over prerequisites and add each to has. Maintain hash of prerequisite->courses
2. When adding a couse check that:
        none of the courses requrie the neCouse being added

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        schedule,visited = {i: [] for i in range(numCourses)}, set()

        for c,p in prerequisites:
            schedule[c].append(p)
        
        def istakeable(c):
            if c not in visited:
                visited.add(c)
                schedule[c] = tuple(p for p in schedule.get(c,[]) if not istakeable(p))
            return not schedule[c]
             
        for c in range(numCourses):
            if not istakeable(c):
                return False
        
        return True
 

class SolutionLeet:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True