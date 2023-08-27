class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while right > left:
            diff = numbers[left] + numbers[right] - target
            if diff == 0:
                return left+1, right+1
            if diff > 0:
                right -= 1
            else:
                left +=1
