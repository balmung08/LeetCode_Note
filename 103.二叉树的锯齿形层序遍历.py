#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
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
        self.res = []
        self.root_list = []
        self.root_list_now = []
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        n = 0
        if root == None:
            return []
        self.root_list = [root]
        def count(i):
            res = []
            while self.root_list:
                i = self.root_list.pop(0)
                if i:
                    res.append(i.val)
                    if i.left:
                        self.root_list_now.append(i.left)
                    if i.right:
                        self.root_list_now.append(i.right)
            # self.root_list_now.reverse()
            self.root_list = self.root_list_now
            self.root_list_now = []
            if n % 2 != 0:
                res.reverse()
            self.res.append(res)
        while self.root_list:
            count(n)
            n += 1
        return self.res
# @lc code=end

