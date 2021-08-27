class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s):
            bit = s[0]
            counts = [0]
            
            for b in s:
                if bit == b:
                    counts[-1] += 1
                else:
                    bit = b
                    counts.append(1)
            
            result = 0
            
            for i in range(1, len(counts)):
                result += min(counts[i - 1], counts[i])
            
            return result
        else:
            return 0
        
