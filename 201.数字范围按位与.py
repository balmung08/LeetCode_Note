#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
# 这么多数里有一个0其实就是0
# 在两个数之间的数都一定会在每一位至少给出一个0
# 因此结果其实是端点数的公共前缀后面补0
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        t = 0   
        while m < n:
            m = m >> 1
            n = n >> 1
            t += 1
        return m << t

        
# @lc code=end

