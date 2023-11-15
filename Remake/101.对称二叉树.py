#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 层序遍历的迭代思路，比较节点是否都存在，存在就比较值
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        q = [(root.left,root.right)]
        while q:
            left, right = q.pop(0)  #先进先出
            #两个都为空，进入下一循环
            if left is None and right is None:
                continue
            #有一个为空，一个不为空，返回False
            if left is None or right is None:
                return False
            #两个都不为空，比较两值是否相等
            if left.val != right.val:
                return False
            q.append((left.left,right.right))
            q.append((left.right,right.left))
        return True

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #左子树的左孩子==右子树的右孩子 and 左子树的右孩子 == 右子树的左孩子
        if root is None:
            return True
        return self.check(root.left,root.right)
    def check(self,left: TreeNode,right: TreeNode):
        #递归的终止条件是两个节点都为空
        #或左右有任意一个不为空，一定不对称
        #两个节点的值不相等
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.check(left.left,right.right) and self.check(left.right,right.left)

# @lc code=end

