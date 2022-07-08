class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i,num in enumerate(nums):            
            dp[i] = max(dp[i-1] + num, num)
        return max(dp)
#         res = nums[0]
        
#         total = 0
#         for n in nums:
#             total += n
#             res = max(res, total)
#             if total < 0:
#                 total = 0
#         return res
        