class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        max_str = ''
        for mid in range(N):
            d = 0
            while mid - d >= 0 and mid + d <= N - 1 and s[mid - d] == s[mid + d]:
                d += 1
            if len(max_str) < 2*d - 1:
                max_str = s[mid - d + 1:mid + d]
        for mid in range(1, N):
            d = 0
            while mid - d >= 0 and mid + d - 1 <= N - 1 and s[mid - d] == s[mid + d - 1]:
                d += 1
            if len(max_str) < 2*d - 2:
                max_str = s[mid - d + 1:mid + d - 1]
        return max_str
