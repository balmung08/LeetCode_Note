'''
class Solution:
    def stockManagement(self, stock: List[int]) -> int:
        return min(stock)
'''
# 根据二分查找，根据中点与尾端的数据比较，可以判断旋转点的位置
class Solution:
    def stockManagement(self, stock: [int]) -> int:
        i, j = 0, len(stock) - 1
        while i < j:
            m = (i + j) // 2
            if stock[m] > stock[j]: i = m + 1
            elif stock[m] < stock[j]: j = m
            else: return min(stock[i:j])
        return stock[i]
