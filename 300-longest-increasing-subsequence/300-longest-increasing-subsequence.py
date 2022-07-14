class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [nums[0]]
        len_dp = 1
        for i in range(1, len(nums)):
            left, right = 0, len(dp) - 1
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if dp[left] < nums[i]:
                dp.append(nums[i])
                len_dp += 1
            else:
                dp[left] = nums[i]
        return len_dp
        
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             if dp[i] < dp[j] + 1:
        #                 dp[i] = dp[j] + 1
        # return max(dp)