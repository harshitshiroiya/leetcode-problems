class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
        
        dp = [0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]
#         if n <= 3: return n
#         n1, n2 = 2, 3
        
#         for i in range(4, n + 1):
#             temp = n1 + n2
#             n1 = n2
#             n2 = temp
#         return n2