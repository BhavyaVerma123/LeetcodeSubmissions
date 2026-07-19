class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                return True
        return False