class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        INT_MIN = -(1 << 31)
        INT_MAX = (1 << 31) - 1
        sign = (x < 0)
        y = [x, -x][sign]
        s = ''
        while y > 0:
            s += str(y % 10)
            y = int(y / 10)
        result = int(s) * [1, -1][sign]
        if result > INT_MAX or result < INT_MIN: return 0
        else: return result
