class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1: return N
        result = 1
        current = nums[0]
        for index in range(1, N):
            if current != nums[index]:
                current = nums[index]
                nums[result] = current
                result += 1
        return result
