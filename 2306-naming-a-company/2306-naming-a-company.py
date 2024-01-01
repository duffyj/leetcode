class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        validNames = set()
        res = 0
        ideasByPrefix = {}
        initialIdeas = set(ideas)
        for i in ideas:
            prefix = i[:1]
            if prefix not in ideasByPrefix:
                ideasByPrefix[prefix] = set()
            ideasByPrefix[prefix].add(i[1:])    
        
        for prefix1, suffixes in ideasByPrefix.items():
            for prefix2,otherIdeas in ideasByPrefix.items():
                if prefix1 == prefix2:
                    continue
                nValidIdea1s = (len(suffixes - ideasByPrefix[prefix2])) 
                nValidIdea2s = (len(otherIdeas) - len(otherIdeas.intersection(ideasByPrefix[prefix1])))
                res += nValidIdea1s * nValidIdea2s
        return res 

    def distinctNamesv1(self, ideas: List[str]) -> int:
        validNames = set()
        ideasByPrefix = {}
        for i in ideas:
            prefix = i[:2]
            if prefix not in ideasByPrefix:
                ideasByPrefix[prefix] = []
            ideasByPrefix[prefix].append()    
        initialIdeas = set(ideas)
        while len(ideas) > 1:
            idea1,otherIdeas = ideas[0],ideas[1:]
            for idea2 in otherIdeas:
                if idea1[:2] != idea2[:2]: 
                    for i1,i2 in (idea1,idea2),(idea2,idea1):
                        i1, i2 = list(i1),list(i2)
                        i1[0], i2[0] = i2[0], i1[0]
                        i1, i2 = ''.join(i1), ''.join(i2)
                        if i1 not in initialIdeas and i2 not in initialIdeas:
                            validNames.add(' '.join((i1,i2)))
            ideas = otherIdeas
        return len(validNames)
