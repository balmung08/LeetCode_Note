#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
# 递归的翻转，前序后序都可以
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right = root.right,root.left
        return root
'''
# 迭代法
# 一层一层的交换
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        stack = [root]
        # 根据
        while stack:
            # 当前节点出栈
            node = stack.pop()
            # 将当前节点的左右子树交换
            node.left, node.right = node.right, node.left
            # 右子树入栈
            if node.right:
                stack.append(node.right)
            # 左子树入栈
            if node.left:
                stack.append(node.left)
        return root

# @lc code=end

