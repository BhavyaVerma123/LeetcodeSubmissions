class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        res = [""] * numRows
        going_down = False
        current_row = 0

        for char in s:
            res[current_row] += char

            if current_row == 0 or current_row == numRows-1:
                going_down = not going_down

            if going_down:
                current_row += 1
            else:
                current_row -= 1

        return "".join(res)