# 快速幂的标准解法，奇数化为偶数，偶数化为一半的次数
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n>0: 
            if n & 1:
                return x * self.myPow(x, n - 1)
            else:
                return self.myPow(x*x, n // 2)
        elif n<0:
            return 1/self.myPow(x,abs(n))