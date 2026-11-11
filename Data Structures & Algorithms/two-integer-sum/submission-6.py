class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maybe = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in maybe:
                return [maybe[diff], i]
            maybe[n] = i