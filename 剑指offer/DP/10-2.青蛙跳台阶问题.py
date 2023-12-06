class Solution:
  def trainWays(self, num: int) -> int:
      if num == 0:
        return 1
      dp = [0] * (num + 1)
      dp[0] = dp[1] = 1
      for i in range(2, num + 1):
          dp[i] = dp[i - 1]%1000000007 + dp[i - 2]%1000000007
      return dp[-1]%1000000007