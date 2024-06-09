#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 算左右子树，大于0的就计入
# 如果都小于0，直接计算当前节点，
# 如果当前节点也小于0则仅保留目前节点
# 并使用一个值最大值，统计左子树、右子树、本节点、上次最大值
class Solution:
    def __init__(self):
        self.max = -9999999999
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def sumtree(root):
            if not root:
                return 0
            s1 = sumtree(root.left)
            s2 = sumtree(root.right)
            s = root.val
            if s1>0 and s2>0:
                s += max(s1,s2) 
            elif s1>0:
                s += s1
            elif s2>0:
                s += s2
            self.max = max(self.max,root.val,root.val+s1,root.val+s2,root.val+s1+s2)
            return s
        sumtree(root)
        return self.max
# @lc code=end

