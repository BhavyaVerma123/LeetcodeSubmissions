class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mpp = {}
        for i in range(len(nums)):
            more = target - nums[i]
            if more in mpp:
                return [mpp[more],i]
            mpp[nums[i]] = i
        return [-1,-1]
        