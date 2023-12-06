class Solution:
    def maxSales(self, sales: List[int]) -> int:
        n = len(sales)
        dp = [0]*(n)
        for i in range(0,n):
            dp[i] = max(dp[i-1],0)+sales[i]
        return max(dp)