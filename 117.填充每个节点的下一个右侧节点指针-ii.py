#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def __init__(self):
        self.root_list = []
        self.root_list_now = []
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        self.root_list = [root]
        def count():
            res = []
            while self.root_list:
                i = self.root_list.pop(0)
                if i and i.left:
                    self.root_list_now.append(i.left)
                if i and i.right:
                    self.root_list_now.append(i.right)
            self.root_list = self.root_list_now
            self.root_list_now = []
            for i in range(len(self.root_list)-1):
                self.root_list[i].next = self.root_list[i+1]
        while self.root_list:
            count()
        return root
        
# @lc code=end


























