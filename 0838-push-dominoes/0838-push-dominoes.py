class Solution:
    def pushDominoes(self, doms: str) -> str:
        n = len(doms)
        q = deque()
        doms = list(doms)
        for i,d in enumerate(doms):
            if d != '.':
                q.append((i,d))
        while q:

            i,d = q.popleft()
            if d == 'L':
                if i > 0 and doms[i-1] == '.':
                    doms[i-1] = 'L'
                    q.append((i-1,'L'))
            else:
                if (i + 1) < n and doms[i+1] == '.':
                    if  (i + 2) < n and doms[i+2] == 'L':
                        q.popleft()
                    else:
                        doms[i+1] = 'R'
                        q.append((i+1,'R'))      

        return ''.join(doms)
        

        