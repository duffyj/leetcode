
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        resCount = 0
        total = 0
        dic = {}
        dic[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            resCount += dic.get(total-k,0)
            dic[total] = dic.get(total, 0)+1
        return resCount



class Solutio2n:
    def subarraySum(self, nums: List[int], k: int) -> int:
        resCount = 0
        prefix = {0:1}
        currTotal = 0
        for n in nums:
            currTotal+=n
            req = currTotal - k
            if req in prefix:
                resCount += prefix[req]
            prefix[currTotal]  = prefix.get(currTotal,0) + 1    
        return resCount
            



class SolutionBruteAgainTLE:
    def subarraySum(self, nums: List[int], k: int) -> int:
        resCount = 0
        subArrayTotals = [0] * len(nums)
        for i,n in enumerate(nums):
            for j in range(i+1):
                subArrayTotals[j] += n
                if subArrayTotals[j] == k:
                    resCount +=1 
        return resCount
            


class SolutionTLE:
    def subarraySum(self, nums: List[int], k: int) -> int:
        resCount = 0
        subArrayTotals = []
        for i,n in enumerate(nums):
            newSubArrayTotals = [0] * (len(subArrayTotals))
            for j in range(len(subArrayTotals)):
                newSubArrayTotals[j] = subArrayTotals[j] + n
                if newSubArrayTotals[j] == k:
                    resCount +=1 
            newSubArrayTotals.append(n)
            if n == k:
                resCount +=1
            subArrayTotals = newSubArrayTotals
        return resCount



class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = nums[0]
        lhs = 0
        rhs = 0
        res = 0
        while lhs <= len(nums)-1:
            if total == k:
                res += 1
            if total >= k or rhs == len(nums)-1:
                total -= nums[lhs]
                lhs += 1
            else:
                rhs += 1
                total += nums[rhs]
        return res

        