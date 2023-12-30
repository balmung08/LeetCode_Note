# 前缀积乘后缀积
class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        n=len(arrayA)
        res=[0]*n
        k=1
        for i in range(n):
            res[i]=k
            k=k*arrayA[i]
        k=1
        for i in range(n-1,-1,-1):
            res[i]*=k
            k*=arrayA[i]
        return res
        