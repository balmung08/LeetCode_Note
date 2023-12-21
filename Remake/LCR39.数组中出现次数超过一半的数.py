'''
# 可以使用哈希表进行统计

# 使用排序
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        stock.sort()
        return stock[len(stock)//2]
'''
# 摩尔投票法
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        votes = 0
        for num in stock:
            if votes == 0: 
                x = num
            votes += 1 if num == x else -1
        return x
