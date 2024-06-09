#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def counter(root):
            if root == None:
                return
            self.res+=1
            counter(root.left)
            counter(root.right)
        counter(root)
        return self.res
# @lc code=end

