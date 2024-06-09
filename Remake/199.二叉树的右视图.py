#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 返回每一层最右边的节点
class Solution:
    def __init__(self):
        self.res = []
        self.root_list = []
        self.root_list_now = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.root_list = [root]
        def count():
            res = []
            while self.root_list:
                i = self.root_list.pop(0)
                if i:
                    res.append(i.val)
                    if i.left:
                        self.root_list_now.append(i.left)
                    if i.right:
                        self.root_list_now.append(i.right)
            self.res.append(res[-1])
            self.root_list = self.root_list_now
            self.root_list_now = []
        while self.root_list:
            count()
        return self.res
# @lc code=end

