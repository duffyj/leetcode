class Solution:
    def canPartition(self, nums: List[int]):
        sm = sum(nums)
        n = len(nums)
        if sm % 2:
            return False
        half = sm // 2

        totals = set((0,))
        for n in nums:
            for t in tuple(totals):
                if t + n == half:
                    return True
                totals.add(t + n)
                print(len(totals))



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            print(len(nextDP))
            dp = nextDP
            
        return False

class Solution2:
    def canPartition(self, nums: List[int]):
        sm = sum(nums)
        n = len(nums)
        if sm % 2:
            return False
        half = sm // 2

        def dfs(total,i,c):
            print (half,total,i,c)
            if total == half or total + nums[i] == half:
                return True
            if i < n -1:

                return any(
                            (
                            dfs(total,i+1, c) if c < n-1 else None,
                            dfs(total+ nums[i],i+1,c+1) if  c+1 < n-1 else None,
                            )
                          )
        
        return dfs(0,0,0)


        