class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        index = len(s) - 1
        while (index >= 0 and s[index] == ' '):
            index -= 1
        if index == -1:
            return 0
        result = 0
        while (index >= 0 and s[index] != ' '):
            index -= 1
            result += 1
        return result
