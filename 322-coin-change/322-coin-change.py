class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]

#         dp = [amount + 1] * (amount + 1) 
#         dp[0] = 0

#         for a in range(1, amount + 1):
#             for c in coins:
#                 if a - c >= 0:
#                     dp[a] = min(dp[a], 1 + dp[a - c])
#         return dp[amount] if dp[amount] != amount + 1 else -1