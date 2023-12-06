# 注意一下状态转移矩阵的推导
class Solution:
    def crackNumber(self, ciphertext: int) -> int:
      n = len(str(ciphertext))
      dp = [0]*(n+1)
      dp[0] = 1
      dp[1] = 1
      for i in range(1,n):
        if int(str(ciphertext)[i-1])*10+int(str(ciphertext)[i])<=25 and int(str(ciphertext)[i-1])>0:
          print("---")
          dp[i+1] = dp[i-1]+dp[i]
        else:
          print("***")
          dp[i+1] = dp[i]
      return dp[-1]