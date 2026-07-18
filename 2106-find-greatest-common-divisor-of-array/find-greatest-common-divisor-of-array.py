class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = nums[0]
        max_num = nums[0]
        
        for i in nums:
            if i > max_num:
                max_num = i
            elif i < min_num:
                min_num = i

        while max_num != 0:
            temp = max_num
            max_num = min_num % max_num
            min_num = temp

        return min_num