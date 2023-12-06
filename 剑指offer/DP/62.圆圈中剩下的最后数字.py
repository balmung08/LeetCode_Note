# 数学问题，可以直接使用公式推状态转移方程
# f(n,m)=[f(n-1,m)+m]%n
class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        dp = [0]*(num+1)
        for i in range(2,num+1):
            dp[i] = (dp[i-1]+target)%i
        return dp[-1]