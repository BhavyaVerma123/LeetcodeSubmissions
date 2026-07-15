class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return n --> one line solution
        a = n**2
        b = n*(n+1)
        while b != 0:
            temp = b
            b = a%b
            a = temp 
        return a