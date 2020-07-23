class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = (2 ** 31) - 1
        INT_MIN = -(2 ** 31)
        start = 0
        while start < len(s) and s[start] == ' ': start += 1
        if start == len(s): return 0
        if not (s[start] == '+' or s[start] == '-' or '0' <= s[start] <= '9'): return 0
        sign = 1
        if s[start] == '-':
            sign = -1
            start += 1
        elif s[start] == '+':
            start += 1
        end = start
        while end < len(s) and '0' <= s[end] <= '9': end += 1
        if end == start: return 0
        numeric = int(s[start:end]) * sign
        if numeric > INT_MAX: numeric = INT_MAX
        elif numeric < INT_MIN: numeric = INT_MIN
        return numeric
        
