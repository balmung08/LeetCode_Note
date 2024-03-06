#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
# 直接迭代
class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        while res*res<=x:
            res+=1
        return res-1

# 二分查找法
class Solution(object):
    def mySqrt(self, x):
        left, right = 0, x + 1
        # [left, right)
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left - 1

# 数学递推公式：求f(x) = num - x^2的零点
# 牛顿递推公式：Xn+1 = Xn - f(Xn)/f'(Xn)
class Solution(object):
    def mySqrt(self, x):
        num = x
        while num * num > x:
            num = (num + x // num) // 2
        return num
# @lc code=end

