#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def mid_find(root):
            if root == None:
                return 
            mid_find(root.left)
            res.append(root.val)
            mid_find(root.right)
        mid_find(root)
        return res[k-1]



# @lc code=end

