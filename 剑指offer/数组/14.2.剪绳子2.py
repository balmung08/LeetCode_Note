'''
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        dp = [0]*(bamboo_len+1)
        dp[1]=dp[2]=1
        for i in range(bamboo_len+1):
            for j in range(2,i):
                dp[i] = max(dp[i],j*dp[i-j],j*(i-j))
        return dp[-1]%1000000007
'''
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        if bamboo_len <= 3: 
            return bamboo_len - 1
        a, b = bamboo_len // 3, bamboo_len % 3
        if b == 0: 
            return 3**a%1000000007
        if b == 1: 
            return 3**(a - 1) * 4 %1000000007
        return 3**a * 2%1000000007