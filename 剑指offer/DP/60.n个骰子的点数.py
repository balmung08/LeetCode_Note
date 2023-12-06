# 二维DP，维数是总和的计数和骰子的个数
# f(n,s)=f(n-1,s-1)+f(n-1,s-2)+f(n-1,s-3)+f(n-1,s-4)+f(n-1,s-5)+f(n-1,s-6)
class Solution:
    def statisticsProbability(self, num: int) -> List[float]:
        dp = [ [0 for n in range(6*num+1)] for n in range(num+1)]
        for i in range(1,7):
            dp[1][i] = 1
        for i in range(2,num+1):
            for j in range(i,i*6+1):
                # 只有递推公式里的s-3这样的大于0才有意义，不然舍去该项
                for k in range(1,7):
                    if j >= k+1:
                        dp[i][j] +=dp[i-1][j-k]
        return [x/sum(dp[-1][num:6*num+1]) for x in dp[-1][num:6*num+1]]