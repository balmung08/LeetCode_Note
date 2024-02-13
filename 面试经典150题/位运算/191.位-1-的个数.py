#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
# 格式转换+内置函数
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        return n.count('1')

# 去除最后一个1并计数
class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

        
# @lc code=end

