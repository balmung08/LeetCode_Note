'''
# 动态规划解法
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        dp = [0]*(bamboo_len+1)
        dp[1]=dp[2]=1
        for i in range(bamboo_len+1):
            for j in range(2,i):
                dp[i] = max(dp[i],j*dp[i-j],j*(i-j))
        return dp[-1]
'''
# 数学解法：尽可能使竹子的切片长度为3能够达到最大结果
# 根据除以3的余数 0 1 2，可能有三种情况
# 余数为0则直接返回3的a次方
# 余数为1则将一个3和余数1转为2*2
# 余数为2则不转换，3的a次方*2
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        if bamboo_len <= 3: 
            return bamboo_len - 1
        a, b = bamboo_len // 3, bamboo_len % 3
        if b == 0: 
            return int(math.pow(3, a))
        if b == 1: 
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)
