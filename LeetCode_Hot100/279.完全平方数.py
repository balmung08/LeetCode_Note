#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
'''
# 方法一：DP-背包问题
# 使用常规的DP思路，拆分的组件范围由开方确定可能的平方数的范围
import math
class Solution:
    def numSquares(self, n: int) -> int:
        DP = [math.inf]*(n+1)
        DP[0] = 0
        for i in range(0,n+1):
            for c in range(int(math.sqrt(i))+1):
                if DP[i-c*c]+1<=DP[i]:
                    DP[i] = DP[i-c*c]+1
        return DP[-1]
'''
# 任何一个正整数都可以表示成不超过四个整数的平方之和。
# 推论：满足四数平方和定理的数n（正好四个数的情况）必定满足 n=4^a(8b+7)
# 数学知识解法，非常非常快
class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        # 如果a=0，b作为n的开方正好是整数，则直接返回bool(b)，就是1
        # 如果a不为0，则让n在1到根号n下整数之间遍历看是否有b满足
        # 如果有b满足，此时返回2，如果没有则最后返回3
        while a**2 <= n:
            b = int((n - a**2)**0.5)
            if a**2 + b**2 == n:
                return bool(a) + bool(b)
            a += 1
        return 3

# @lc code=end

