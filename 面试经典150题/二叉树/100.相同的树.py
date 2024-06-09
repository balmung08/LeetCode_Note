#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
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
        self.same = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def find(t1,t2):
            if not t1 and not t2:
                return
            elif not t1 or not t2:
                self.same = False
                return              
            if t1.val != t2.val or bool(t1.left) != bool(t2.left) or  bool(t1.right) != bool(t2.right):
                self.same = False
                return 
            if t1.left and t2.left:
                find(t1.left,t2.left)
            if t1.right and t2.right:
                find(t1.right,t2.right)
        find(p,q)
        return self.same
# @lc code=end

