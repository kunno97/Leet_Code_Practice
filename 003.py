'''
Find the two longest substring without repeating characters:
1. Substring that includes the last character
2. Substring in the string (might equal to 1)
And do the recursion
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if N < 2: return N
        s0, s1, t0, t1 = 0, 0, 1, 1
        # s[s0, t0] is substring including the last char
        # s[s1, t1] is substring without conditions
        for index in range(1, N):
            i = -1
            try:
                i = s.index(s[index], s0, t0)
            except:
                t0 += 1
                if t1 - s1 <= t0 - s0: s1, t1 = s0, t0
            else:
                if t1 - s1 < t0 - s0: s1, t1 = s0, t0
                s0, t0 = i + 1, index + 1
        return max(t0 - s0, t1 - s1)
