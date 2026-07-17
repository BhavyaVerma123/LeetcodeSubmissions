class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        low = 0
        high = int(math.sqrt(c))
        while low<=high:
            temp = low**2 + high**2 
            if temp > c:
                high -= 1
            elif temp < c:
                low += 1
            else:
                return True
        return False