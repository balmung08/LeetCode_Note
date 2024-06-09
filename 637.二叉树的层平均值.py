#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 可以使用层序遍历
# 但是为了与层序遍历题目做出区分，此处使用dfs+标记层数与节点数的思路
class Solution:
    def __init__(self):
        self.res = [0]*10001
        self.point = [0]*10001
        self.count = 0
        self.max_len = 0
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def dfs(root,count):
            if root == None:
                return
            dfs(root.left,count+1)
            dfs(root.right,count+1)
            self.res[count]+=root.val
            self.point[count]+=1
            self.max_len = max(count,self.max_len)
        dfs(root,0)
        for i in range(self.max_len+1):
            self.res[i] /= self.point[i]
        return self.res[:self.max_len+1]
# @lc code=end

