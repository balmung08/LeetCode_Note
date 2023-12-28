class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        stock.sort()
        res = []
        for i in range(cnt):
            res.append(stock[i])
        return res

# 不要用内置排序
    