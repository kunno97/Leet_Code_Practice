class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        N = len(s)
        result = list(s)
        l, r = 0, N - 1
        while l < N and s[l] not in vowels: l += 1
        if l == N: return s
        while 0 <= r and s[r] not in vowels: r -= 1
        while l < r:
            result[l], result[r] = result[r], result[l]
            l += 1
            r -= 1
            while l < N and s[l] not in vowels: l += 1
            while 0 <= r and s[r] not in vowels: r -= 1
        return ''.join(result)
