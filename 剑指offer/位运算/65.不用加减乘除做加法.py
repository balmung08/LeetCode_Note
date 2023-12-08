# python的二进制存储比较抽象，重点关注方法即可
# 两个位数的异或可以表示本位，取与可以表示是否有进位
# 两个二进制数的和可以分解为无进位和+进位
# 而无进位和和进位和的1全部不在同一位上，两者取或即可得到答案
class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        x = 0xffffffff
        dataA, dataB = dataA & x, dataB & x
        while dataB != 0:
            dataA, dataB = (dataA ^ dataB), (dataA & dataB) << 1 & x
        return dataA if dataA <= 0x7fffffff else ~(dataA ^ x)