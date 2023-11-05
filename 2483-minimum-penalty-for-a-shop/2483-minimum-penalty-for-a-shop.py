class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalties = []
        postfix = [0] * (len(customers)+1)
        for c in customers:
            if c == 'Y':
                penalties.append((0,1))
            else:
                penalties.append((1,0))
        penalties.append((0,0))
        prior = 0
        for i in range(len(penalties)-1,-1,-1):
            postfix[i] = penalties[i][1] + prior
            prior = postfix[i]
        t = sys.maxsize
        minP = sys.maxsize
        curP  = 0
        for i,(p,closePen) in enumerate(zip(penalties,postfix)):
            if curP  + closePen < minP:
                minP = curP + closePen
                t = i
            curP += p[0]
        return t

        


