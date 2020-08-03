class Solution:
    def reverseString(self, s: List[str]) -> None:
        N = len(s)
        for i in range(int(N / 2)): s[i], s[N - i - 1] = s[N - i - 1], s[i]
