#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited_node = {}
        def dfs(origin_root):
            if origin_root == None:
                return None
            # 不新建节点的原因是要把已经建好的节点接给新节点
            if origin_root in visited_node:
                return visited_node[origin_root]
            New_node = Node(origin_root.val,[])
            visited_node[origin_root] = New_node 
            # 使用for循环可以应对单节点和空节点的情况
            for n in origin_root.neighbors:
                New_node.neighbors.append(dfs(n))
            return New_node
        res = dfs(node)
        return res
        
# @lc code=end

