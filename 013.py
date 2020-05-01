class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        index = 0
        N = len(s)
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        numbers = [1, 5, 10, 50, 100, 500, 1000]
        current = ''
        while index < N:
            current = s[index]
            index += 1
            if current == symbols[6]: result += numbers[6]
            elif current == symbols[5]: result += numbers[5]
            elif current == symbols[4]:
                if index < N and (s[index] == symbols[5] or s[index] == symbols[6]): result -= numbers[4]
                else: result += numbers[4]
            elif current == symbols[3]: result += numbers[3]
            elif current == symbols[2]:
                if index < N and (s[index] == symbols[3] or s[index] == symbols[4]): result -= numbers[2]
                else: result += numbers[2]
            elif current == symbols[1]: result += numbers[1]
            else:
                if index < N and (s[index] == symbols[1] or s[index] == symbols[2]): result -= numbers[0]
                else: result += numbers[0]
        return result
