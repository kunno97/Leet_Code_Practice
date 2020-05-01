class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '{', '[']
        closes = [')', '}', ']']
        stack = []
        for c in s:
            if c in opens: stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != opens[closes.index(c)]: return False
                else: stack.pop()
        return len(stack) == 0
