class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(left, right):
            dp, dp1, dp2 = 0, 0, 0
            for i in range(left, right+1):
                dp = max(dp1, dp2 + nums[i])
                dp2 = dp1
                dp1 = dp
            return dp1
        
        n = len(nums)
        if n == 1: return nums[0]
        return max(solve(0, n-2), solve(1, n-1))
#         return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
#     def helper(self, nums):
#         r1, r2 = 0, 0
        
#         for n in nums:
#             newRob = max(r1 + n, r2)
#             r1 = r2
#             r2 = newRob
#         return r2
      