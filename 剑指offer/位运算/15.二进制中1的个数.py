'''
# python内置函数
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        return n.count("1")
'''
'''
# 无法使用DP思路，因为需要的空间太大，需要位运算方法
# 1.逐位判断
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if bin(n)[-1] == '1':
                res += 1
            n = n >> 1
        return res 
'''
# 2.n&n-1
# n&(n−1) 解析：二进制数字 n最右边的1变成0,其余不变
# 每一次进行这样的变换相当于都消除了一个1
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
