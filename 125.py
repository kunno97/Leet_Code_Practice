class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        if s == None or N < 2: return True
        left = 0
        right = N - 1
        while left < right:
            while left < N and not self.validChar(s[left]): left += 1
            while 0 <= right and not self.validChar(s[right]): right -= 1
            if left == N or right == -1: break
            if not self.sameChar(s[left], s[right]): return False
            left += 1
            right -= 1
        return True
    
    def validChar(self, ch: str) -> bool:
        return ('0' <= ch and ch <= '9') or ('a' <= ch and ch <= 'z') or ('A' <= ch and ch <= 'Z')
    
    def sameChar(self, ch1: str, ch2: str) -> bool:
        if '0' <= ch1 and ch1 <= '9': return ch1 == ch2
        else: return (ch1 == ch2) or (abs(ord(ch1) - ord(ch2)) == abs(ord('a') - ord('A')))
