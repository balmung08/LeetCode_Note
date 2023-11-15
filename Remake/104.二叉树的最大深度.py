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

# 朴素的层序遍历计数思想
# 层序遍历的代码写的很糙
# 思路来自101--102--104
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        Q = [(root.left,root.right)]
        P = []
        temp = []
        res = 1
        while Q:
            left, right = Q.pop(0)  #先进先出
            if left:
                temp.append(left.val)
                if left.left and left.right:
                    P.append((left.left,left.right))
                elif left.left and not left.right:
                    M = (left.left,None)
                    P.append(M)
                elif not left.left and left.right:
                    P.append((None,left.right))
            if right:
                temp.append(right.val)
                if right.left and right.right:
                    P.append((right.left,right.right))
                elif right.left and not right.right:
                    P.append((right.left,None))
                elif not right.left and right.right:
                    P.append((None,right.right))
            if Q == []:
                Q = P.copy()
                P = []
                res+=1
                temp = []
        return res
# @lc code=end

