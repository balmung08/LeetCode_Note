#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
# 在保证能够调到的时候
# 走到边缘了就把之前记录的最远边缘推出来
# 由于走到倒数第二个时，如果是边缘就加一，不是边缘说明最后一个也可以到
# 如果循环到最后一个时且最后一个是边界时会加1再返回
# 最后一个是边界时，要么作判断提前返回要么就仅循环到倒数第二个
# 其实处理方法是一样的，提前返回本质上就是不做最后一次循环
class Solution:
    def jump(self, nums: List[int]) -> int:
        j = 0
        res = 0
        m = 0
        for i in range(len(nums)-1):
            m = max(m,i+nums[i])
            if i == j:
                j = m
                res += 1
        return res

# @lc code=end

