class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first = -1
        second = -1
        index = 0
        
        for idx, num in enumerate(nums):
            if first < num:
                first, second, index = num, first, idx
            elif second < num:
                second = num
        
        if first >= 2 * second:
            return index
        else:
            return -1
