#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 中序遍历秒杀
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def mid_find(root):
            if root == None:
                return 
            mid_find(root.left)
            res.append(root.val)
            mid_find(root.right)
        mid_find(root)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True
# @lc code=end

