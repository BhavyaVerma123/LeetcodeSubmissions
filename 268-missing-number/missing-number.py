class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range (len(nums)+1):
            if i not in nums:
                res = i
                break
        return res