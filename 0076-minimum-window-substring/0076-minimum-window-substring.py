
class Solution:
    def minWindow(self, s: str, t: str):
        if not s or not t:
            return ''
        resLen = sys.maxsize
        resChar = ""
        nS = len(s) 
        nT = len(t)
        resL,resR = None,None
        reqCnt = {}
        for x in t:
            reqCnt[x] = reqCnt.get(x,0) +1

        charsToCount = set(reqCnt.keys())
        cnt = {}
        have = 0
        l = 0
        need = len(charsToCount)
        for r in range(nS):
            rC = s[r]
            if s[r] in charsToCount:
                cnt[rC] = cnt.get(rC,0) + 1
                if cnt[rC] == reqCnt[rC]:
                    have +=1   
                
            while have >= need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    resL,resR = l,r+1     

                lC = s[l]
                if lC in charsToCount:
                    cnt[lC]  -=1
                    if cnt[lC] == (reqCnt[lC] -1):
                        have -=1                     
                l +=1

        return s[resL:resR] if resL != None else ""



class SolutionLeet:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

class SolutionMineSloiw:
    def minWindow(self, s: str, t: str):
        if not s or not t:
            return ''
        resLen = sys.maxsize
        resChar = ""
        nS = len(s) 
        nT = len(t)
        resL,resR = None,None
        reqCnt = {}
        for x in t:
            reqCnt[x] = reqCnt.get(x,0) +1

        charsToCount = set(reqCnt.keys())
        l,r = 0,0
        cnt = {s[0] : 1}
        have = 1 if reqCnt.get(s[0],0) == 1 else 0
        need = len(charsToCount)
        while r < nS and l <= nS-nT:
            if have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    resL,resR = l,r+1
                    if resLen == nT:
                        break
            elif r < nS -1:
                r +=1
                rC = s[r]
                if s[r] in charsToCount:
                    cnt[rC] = cnt.get(rC,0) + 1
                    if cnt[rC] == reqCnt[rC]:
                        have +=1                
                continue
            lC = s[l]
            if lC in charsToCount:
                cnt[lC]  -=1
                if cnt[lC] == (reqCnt[lC] -1):
                    have -=1  
            l +=1

        return s[resL:resR] if resL != None else ""

class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        letter_counts = {}
        remaining = len(t)
        for letter in t:
            letter_counts[letter] = 1 + letter_counts.get(letter, 0)

  
        global_queue = deque()
        l_min, r_min = 0, float('inf')
        start = None
        for i, char in enumerate(s):
            if char in letter_counts:
                global_queue.append(i)
                if start is None:
                    start = global_queue.popleft()
                letter_counts[char] -= 1
                if letter_counts[char] < 0:
                    # We have more of this char than we need
                    if s[start] == char:
                        while letter_counts[s[start]] < 0:
                            letter_counts[s[start]] += 1
                            start = global_queue.popleft()
                else:
                    # We are still in need of this char
                    remaining -= 1
                if remaining == 0 and (i - start) < (r_min - l_min):
                    l_min, r_min = start, i

        return s[l_min:r_min + 1] if r_min != float('inf') else ''