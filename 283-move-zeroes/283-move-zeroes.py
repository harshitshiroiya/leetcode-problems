class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for j in range(n):
            if (nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1