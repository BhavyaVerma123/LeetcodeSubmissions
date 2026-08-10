class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currsum = nums[0]
        maxsum = nums[0]

        for i in nums[1:]:
            currsum = max(i,currsum+i)
            maxsum = max(maxsum,currsum)

        return maxsum