class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            # do search
            l = i+1
            r = n -1
            while l < r:
                diff = nums[i] + nums[l] + nums[r]
                if diff ==0:
                    results.add((nums[i],nums[l],nums[r]))
                    l +=1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1 # move to a new triple
                elif diff > 0:
                    r -=1
                else:
                    l +=1
        return results




class SolutionNew:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        vals = {n : i for i,n in enumerate(nums)}
        n = len(nums) -1
        results = set()

        l = 0
        while l < n:
            r = l+1
            while r < n:
                target = -(nums[l] + nums[r])
                if target in vals and vals[target] > r:
                    triplet = [nums[l],nums[r],target]
                    triplet.sort()
                    results.add(tuple(triplet))
                r+=1
            l+=1
        return results

class SolutionOld:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        vals = {}
        res = set()
        l = 0
        n = len(nums) -1
        
        while l <=n :
            vals[nums[l]] = l
            l += 1

        l = 0
        while l < n:
            r = l +1
            while r < n:
                target = -(nums[l] + nums[r])
                if target in vals and vals[target] > r:
                    toAdd = [nums[l],nums[r], target]
                    toAdd.sort()       
                    res.add(tuple(toAdd))
                r += 1
            l += 1 
        return list(res)

class SolutionLeet:
    def threeSum(self, integers):
        """
        :type integers: List[int]
        :rtype: List[List[int]]
        """
        integers.sort()
        result = []
        for index in range(len(integers)):
            if integers[index] > 0:
                break
            if index > 0 and integers[index] == integers[index - 1]:
                continue
            left, right = index + 1, len(integers) - 1
            while left < right:
                if integers[left] + integers[right] < 0 - integers[index]:
                    left += 1
                elif integers[left] + integers[right] > 0 - integers[index]:
                    right -= 1
                else:
                    result.append([integers[index], integers[left], integers[right]]) # After a triplet is appended, we try our best to incease the numeric value of its first element or that of its second.
                    left += 1 # The other pairs and the one we were just looking at are either duplicates or smaller than the target.
                    right -= 1 # The other pairs are either duplicates or greater than the target.
                    # We must move on if there is less than or equal to one integer in between the two integers.
                    while integers[left] == integers[left - 1] and left < right:
                        left += 1 # The pairs are either duplicates or smaller than the target.
        return result
        
