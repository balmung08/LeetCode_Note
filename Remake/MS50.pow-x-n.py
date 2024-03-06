#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
'''
# 按常规迭代解法会超时
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n>0:
            for i in range(n):
                res = res*x
            return res
        else:
            for i in range(abs(n)):
                res = res*x
            return 1/res
'''
# 快速幂
# 如何判断是否需要补1是问题的关键
# 根据二进制进行判断（找规律）
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

# @lc code=end

