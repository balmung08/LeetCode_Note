#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 先中序遍历，得到列表后更新相邻元素的最小差值
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        def mid_find(root):
            if root == None:
                return 
            mid_find(root.left)
            res.append(root.val)
            mid_find(root.right)
        mid_find(root)
        ans = 999999
        for i in range(1,len(res)):
            ans = min(ans,abs(res[i]-res[i-1]))
        return ans
# @lc code=end

