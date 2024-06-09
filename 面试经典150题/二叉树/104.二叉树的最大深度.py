#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
        self.M = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find(first,n):
            if first.left == None and first.right==None:
                self.M = max(self.M,n)
            if first.left:
                find(first.left,n+1)
            if first.right:
                find(first.right,n+1)
        if root:
            find(root,1)
            return self.M
        return 0

# @lc code=end

