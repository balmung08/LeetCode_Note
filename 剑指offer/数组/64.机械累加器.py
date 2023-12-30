# 不能使用迭代就只能递归了
# 不能使用if就只能用and的性质了
# python的 and 操作如果最后结果为真，返回最后一个表达式的值
# or 操作如果结果为真，返回第一个结果为真的表达式的值
# 官解的快速乘手写循环纯扯淡了
class Solution:
    def mechanicalAccumulator(self, target: int) -> int:
        return target >=1 and target+self.mechanicalAccumulator(target+(-1)) 