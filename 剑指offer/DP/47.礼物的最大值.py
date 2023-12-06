# 和LC64一模一样，把最小换成最大即可
class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        m = len(frame)#行
        n = len(frame[0])#列
        dp = [[0 for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            res += frame[i][0]
            dp[i][0] = res
        res = 0
        for i in range(n):
            res += frame[0][i]
            dp[0][i] = res
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])+frame[i][j]
        return dp[-1][-1]