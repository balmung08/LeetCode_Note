#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,count):
            count += root.val
            if root.left == None and root.right == None:
                self.res += count
                return
            if root.left:
                dfs(root.left,count*10)
            if root.right:
                dfs(root.right,count*10)

        dfs(root,0)
        return int(self.res)

# @lc code=end

