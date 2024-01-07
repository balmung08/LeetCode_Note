#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
'''
# 完全模拟法
# 实现是对的但是会超时
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            Q = 0
            j = i
            while True:
                Q += gas[j]
                if Q-cost[j]<0:
                    break
                Q -= cost[j]
                j += 1
                if j>=len(gas):
                    j = 0
                if j == i:
                    return i
        return -1
'''
# https://leetcode.cn/problems/gas-station/description/comments/457040
# 很有意思的讲解
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        # a 就是那个数组
        a = []
        for i in range(len(gas)):
            a.append(gas[i] - cost[i])

        # 选一个能赚油点的点开始计算
        # 如果到某个点走不动了，开始到结束这一段区域均不可行
        # 从下一个点开始直到能走到结束
        # 此时因为整体是不亏的，所有后面赚的一定能把前面亏的补回来
        if sum(a) < 0:
            return -1

        start = 0
        all_money = 0
        for i in range(len(a)):
            all_money += a[i]
            if all_money < 0:
                all_money = 0
                start = i+1

        return start
# @lc code=end

