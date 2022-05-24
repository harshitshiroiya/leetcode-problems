class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=float('+inf')
        profit=0
        today=0
        for i in range(len(prices)):
            if prices[i] < minn:
                minn=prices[i]
            today=prices[i]-minn
            if today > profit:
                profit=today
        return profit