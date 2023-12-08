#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0,n+1):
            i = bin(i)
            res.append(i.count("1"))
        return res
# DP解法
# 奇数的1永远比其上一个偶数多1
# 偶数的第一位为0，因此把它除以二以后1的个数不变
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(1,num+1):
            if(i%2==1):
                dp[i]=dp[i-1]+1
            else:
                dp[i]=dp[i//2]
        return dp

# @lc code=end

