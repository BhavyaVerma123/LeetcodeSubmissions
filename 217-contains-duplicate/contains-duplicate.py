class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique = set(nums)
        if len(unique) == len(nums):
            return False
        return True