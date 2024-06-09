#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
        self.res = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def compare(root,s):
            if root == None:
                return
            if root.left == None and root.right == None:
                if s+root.val == targetSum:
                    self.res = True
                    return
                return
            compare(root.left,s+root.val)
            compare(root.right,s+root.val)
        compare(root,0)
        return self.res
                 
# @lc code=end

