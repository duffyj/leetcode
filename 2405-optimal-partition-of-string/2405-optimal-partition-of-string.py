class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        subs = set()
        for c in s:
            if c in subs:
                subs = set(c)
                res +=1 
            else:
                if not subs:
                    res +=1 
                subs.add(c)
        return res
            

class SolutionMineCrap:
    def partitionString(self, s: str) -> int:
        partitaions = [[]]
        for c in s:
            newPartitaions = []
            for p in partitaions:
                newPartitaions.append(p)
                if c not in p:
                    newPartitaions.append(p[:] + [c])
            partitaions = newPartitaions[:]
        
        x = set([''.join(sorted(p)) for p in partitaions])
        return len(x)

