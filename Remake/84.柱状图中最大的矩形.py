#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start

# 从原则上来说一定是某个柱子的高度往左右扩散
# 因此最后结果是某个柱子的高度乘上其左右两边连续且高于它本身的宽度和
# 因此可以依次遍历每个柱子并每次往两边扩散，但是复杂度太高
# 可以使用单调栈存储柱子的编号
# 注意右边界的细节和前后补0的作用
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
                print(stack)
            stack.append(i)
        return res

            
55563
# @lc code=end

