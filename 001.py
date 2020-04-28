class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                if target == nums[i] + nums[j]: return [i, j]
