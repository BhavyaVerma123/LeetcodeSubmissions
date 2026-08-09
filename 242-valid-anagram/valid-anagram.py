class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mpp = {}
        for i in range(len(s)):
            if s[i] not in mpp:
                mpp[s[i]] = 1
            else:
                mpp[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in mpp or mpp[t[i]] == 0:
                return False
            else:
                mpp[t[i]] -= 1
        return True