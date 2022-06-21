class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            ele = nums[mid]
            if ele > nums[high]:
                low = mid + 1
            elif mid == 0 or nums[mid - 1] > nums[mid]:
                return nums[mid]
            else:
                high = mid - 1