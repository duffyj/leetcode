"""
[[1,0] [1,2] , [1,3]] = take 3,2,0 and then 1
[[1,0] [1,2] , [1,3], [1,1]] = take not possible

1. loop over prerequisites and add each to has. Maintain hash of prerequisite->courses
2. When adding a couse check that:
        none of the courses requrie the neCouse being added

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        schedule = dict()
        visited = set()

        def istakeable(c):
            if c not in visited:
                visited.add(c)
                newPrerequisites = []
                for p in schedule.get(c,[]):
                    if not istakeable(p):
                        newPrerequisites.append(p)
                schedule[c] = newPrerequisites
            return not schedule[c]
             

        for c,p in  prerequisites:
            schedule[c] = schedule.get(c,[]) + [p]
        
        for c in range(numCourses):
            if istakeable(c):
                numCourses-= 1
        
        return numCourses <= 0
 

