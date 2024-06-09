#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1.可以直接前序遍历再重新构造节点，这是最简单的方法

# 2.把右子树接到左子树的最下右根节点
# 要找到右下节点，得记录一下前一个节点
# 当其节点到空时直接返回前一个节点
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def find(root,pre):
            
            if root == None:
                return pre
            # 用于先处理好右子树
            # 随后处理左子树，再把右子树拼过去
            pre = find(root.right, pre)
            pre = find(root.left, pre)
            root.right = pre
            root.left = None
            # 处理完了以后也得返回根节点
            # 不然没法把最底下的这个节点一路返回到最顶上的递归
            return root
        find(root,None)
# @lc code=end

