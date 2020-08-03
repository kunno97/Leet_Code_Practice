class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N = len(nums)
        p1, p2 = 0, 0
        while p2 < N:
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1
