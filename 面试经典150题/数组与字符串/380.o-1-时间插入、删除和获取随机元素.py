#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
'''
# 如果全部使用dict，则随机输出需要转为列表的这一步复杂度超了
import random
class RandomizedSet:
    def __init__(self):
        self.L = {}
    def insert(self, val: int) -> bool:
        if val in self.L:
            return False
        else:
            self.L[val] = True
            return True
    def remove(self, val: int) -> bool:
        if val in self.L:
            self.L.pop(val)
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.sample(list(self.L.keys()), 1)[0]
'''
# 字典列表混用，字典用于存储列表的元素的位置
# 删除时先交换序列号再交换数值，在交换数值时弹出序列号，最后单独弹出数值
import random
class RandomizedSet:
    def __init__(self):
        self.L = {}
        self.num = []
    def insert(self, val: int) -> bool:
        if val in self.L:
            return False
        else:
            self.L[val] = len(self.num)
            self.num.append(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.L:
            self.L[self.num[-1]] = self.L[val]
            self.num[self.L.pop(val)] = self.num[-1]
            self.num.pop()
            return True
        else:
            return False
    def getRandom(self) -> int:
        return self.num[random.randint(0, len(self.num) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

