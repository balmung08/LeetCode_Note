#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        # int函数实际上是有第二个参数的，表示按照什么进制转换为整数
        return int(bin(n)[2:].zfill(32)[::-1],2)
'''
class Solution:
    def reverseBits(self, n):
        ans = 0
        for _ in range(32):
        #按顺序读出n的每一位(最低位)，并加到当前ans的结果中。
        #然后将ans整体左移，将之前获得的值整体上移一位，这里就实现了逆序。
        #对于n，就整体下移一位，右移一位，为下一次读最低位做准备。
            ans <<= 1
            ans += (n&1)
            n >>=1
        return ans

        
# @lc code=end

