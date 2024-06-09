#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 拆成均匀的两半，随后按倒序压到两侧
# 每个节点下的子树都必须满足平衡的要求
# 因此需要递归
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(nums,First):
            mid = len(nums)//2
            l_side = nums[:mid]
            r_side = nums[mid+1:]
            # print(l_side,r_side)
            if l_side != []: 
                First.left = TreeNode(l_side[len(l_side)//2])
                divide(l_side,First.left)
            if r_side != []:
                First.right = TreeNode(r_side[len(r_side)//2])
                divide(r_side,First.right)

        mid = len(nums)//2
        First = TreeNode(nums[mid])
        divide(nums,First)
        return First

# @lc code=end

