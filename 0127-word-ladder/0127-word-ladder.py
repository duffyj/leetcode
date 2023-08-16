
from functools import lru_cache

def diffMaps(c):
    def pat(x1):
        return (c[:x1],'*', c[x1+1:])
    return tuple(pat(x) for x in range(len(c)))

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]):
        if endWord not in wordList:
            return 0

        allwords = [beginWord] + wordList
        adjacents = collections.defaultdict(list)
        for w in allwords:
                for j in range(len(w)):
                    pattern = w[:j] + "*" + w[j + 1 :]
                    adjacents[pattern].append(w)
            
        queue = deque([beginWord])
        visited = set([beginWord])
        wordCount = 1         
        while queue:
            for _ in range(len(queue)):
                toSearch = queue.popleft()      
                if toSearch == endWord:
                    return wordCount        
                for j in range(len(toSearch)):
                    pattern = toSearch[:j] + "*" + toSearch[j + 1 :]
                    for newWrd in adjacents[pattern]:
                        if newWrd not in visited:
                            visited.add(newWrd)
                            queue.append(newWrd)

            wordCount+=1        
        return 0

class SolutionLeet:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0


from sys import maxsize
if False:

    @lru_cache()
    def chardiff(w1,w2):
        diff = 0
        for c1, c2 in zip(w1,w2):
            if c1 != c2:
                diff+=1
        return diff

    class Solution2:
        def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            if endWord not in wordList:
                return 0

            allwords = [beginWord] + wordList
            adjacents = {w:set() for w in set(allwords)}
            for i,w1 in enumerate(allwords):
                for w2 in allwords[i:]:
                    if w1 == w2:
                        continue
                    if chardiff(w1,w2)== 1:
                        adjacents[w1].add(w2)
                        adjacents [w2].add(w1)
            

            minpath = [maxsize]
            def dfs(w,path):
                if len(path) + 1 < minpath[0]:
                    if w == endWord:
                        minpath[0] = min(minpath[0],len(path)+1)
                        return
                    path = set(path)
                    path.add(w)
                    for adjW in (adjacents[w] - set(path)):
                        dfs(adjW,set(path))
            dfs(beginWord,set())
            return minpath[0] if minpath[0] != maxsize else 0


from functools import lru_cache

def diffMapsOLD(c):
    def pat(x1):
        return (c[:x1],'*', c[x1+1:])
    return tuple(pat(x) for x in range(len(c)))


class SolutionSlow70Percent:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]):
        if endWord not in wordList:
            return 0

        allwords = [beginWord] + wordList
        adjacents = collections.defaultdict(list)
        for w in allwords:
            for pattern in diffMaps(w):
                adjacents[pattern].append(w)
            
        queue = deque([beginWord])
        visited = set([beginWord])
        wordCount = 1         
        while queue:
            for _ in range(len(queue)):
                toSearch = queue.popleft()      
                if toSearch == endWord:
                    return wordCount        
                for pat in diffMaps(toSearch):
                    for newWrd in adjacents[pat]:
                        if newWrd not in visited:
                            visited.add(newWrd)
                            queue.append(newWrd)

            wordCount+=1        
        return 0
