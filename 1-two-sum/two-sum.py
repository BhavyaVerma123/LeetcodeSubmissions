class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mpp = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mpp:
                return [mpp[diff],i]
            mpp[nums[i]] = i
        return []