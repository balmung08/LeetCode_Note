#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        Q = [(root.left,root.right)]
        P = []
        temp = []
        res = [[root.val]]
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
                res.append(temp)
                temp = []
        return res
# @lc code=end

