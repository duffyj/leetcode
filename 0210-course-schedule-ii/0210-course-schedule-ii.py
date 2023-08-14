class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        courses = list(range(numCourses))
        schedule,visited = {i: [] for i in range(numCourses)}, set(courses)

        for c,p in prerequisites:
            visited.discard(c)
            schedule[c].append(p)
        
        result = list(visited)
        cycle = set()
        for c,p in prerequisites:
            schedule[c].append(p)
        
        def istakeable(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            for p in schedule[c]:
                if not istakeable(p):
                    return False
            cycle.remove(c)
            visited.add(c)
            result.append(c)
            return True
             
        for c in range(numCourses):
            if not istakeable(c):
                return []
        
        return result



class SolutionLeetMine:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        courses = list(range(numCourses))
        schedule,visited = {i: [] for i in range(numCourses)}, set(courses)

        for c,p in prerequisites:
            visited.discard(c)
            schedule[c].append(p)
        
        result = list(visited)
        cycle = set()

        for c,p in prerequisites:
            schedule[c].append(p)
        
        def istakeable(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            
            cycle.add(c)
            for p in schedule[c]:
                if  not istakeable(p):
                    return False
            cycle.remove(c)
            visited.add(c)
            result.append(c)
            return True
             
        for c in range(numCourses):
            if not istakeable(c):
                return []
        
        return result
