#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 每一层的时候将之前的路径加上本次节点，并在路径节点后加入本次节点
# 表示以当前节点结尾的所有可能路径
# 因此不能等结束再统计，必须一边递归就一边统计了 
class Solution:
    def __init__(self):
        self.res = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root,sumlist):
            if root is None:
                return 0
            sumlist = [num+root.val for num in sumlist]
            sumlist.append(root.val)
            for i in sumlist:
                if i == targetSum:
                    self.res += 1
            dfs(root.left,sumlist)
            dfs(root.right,sumlist)
        dfs(root,[])
        return self.res 
# @lc code=end

