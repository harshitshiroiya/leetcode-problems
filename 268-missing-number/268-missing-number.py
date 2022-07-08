class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum1 = 0
        # n = len(nums)
        # a = (n) * (n + 1) // 2
        # for i in range(n):
        #     sum1 = sum1 + nums[i]
        # return a - sum1
        
        return sum(range(len(nums)+1)) - sum(nums)