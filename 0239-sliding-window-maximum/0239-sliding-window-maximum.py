class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxes = deque()
        res = []
        l = r = 0 
        n = len(nums)

        while r < n:
            while maxes and nums[maxes[-1]] < nums[r]:
                maxes.pop()
            maxes.append(r)

            if l > maxes[0]:
                maxes.popleft()
            
            if r+1 >= k:
                res.append(nums[maxes[0]])
                l += 1
            r +=1

        return res

            
class SolutionFcked:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        """ for each i
        if maxes. empty:
             append  the value to mmaxes
        else:
            if current num < than maxces[-1]:
                mazes.pop()
            append  the value to mmaxes
        if k i paset start of window:
            add maze[0] to results
        """
        maxes = deque()
        res = []
        
        for i in range(len(nums)):
            nI = nums[i]
            if not maxes:
                maxes.append(nI)
            else:
                if nI >= maxes[-1]:
                    maxes.pop()
                    maxes.append(nI)
            if i > k:
                res.append(maxes[0])
        return res
        


class SolutionFailed1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        nN = len(nums)
        maxes = deque()
        r,l = 0,0
    
        """
        if oldLVal == letf of maxes then popleft maxes
            newmax is max of (new left of deque, right of deque, new rVal)
        if newmax > right of deque:
            pushleft newmqx

        append right of deque to results
        """

        # Load deque
        startMax = nums[0]       
        for i in range(k):
            startMax = max(startMax,nums[i])
            if not maxes or startMax > maxes[-1]:
                maxes.append(startMax)

        results = [startMax]
        for r in range(k, len(nums)):
            if  maxes[-1] == nums[r-k]:
                maxes.popleft()
            if maxes:
                newmax= max(maxes[0],nums[r])
                if newmax > maxes[0]:
                    maxes.append(newmax)
            else:
               maxes.append(nums[r]) 
            results.append(maxes[-1])

        return results




