class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
#         dp = [amount + 1] * (amount + 1) 
#         dp[0] = 0

#         for a in range(1, amount + 1):
#             for c in coins:
#                 if a - c >= 0:
#                     dp[a] = min(dp[a], 1 + dp[a - c])
#         return dp[amount] if dp[amount] != amount + 1 else -1