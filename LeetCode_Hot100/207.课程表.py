#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
# 判断有向图是否存在环

'''
# DFS
对numCourses个节点依次执行 DFS，判断是否存在环，若存在环直接返回 False
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True
'''

# BFS，拓扑排序
# 注意入度的概念
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        ind = [0]*numCourses
        # 将前置课为key，当前课为value
        for a,b in prerequisites:
            g[b].append(a)
            # 记录此课已经被遍历过了
            ind[a]+=1
        # 开始找环，首先把没有被遍历过的课程的序号提取出来
        # 无环情况下只有可能是头和尾
        queue = [i for i in range(numCourses) if ind[i] == 0]
        count = 0
        # 入度为0的课可以直接选，不然的话得等入度变为0
        while queue:
            i = queue.pop()
            count += 1
            # 选了入度为0的课以后，把其后置课程的入度减1
            # 减到0为止他就可以被选了，加入队列
            for j in g[i]:
                ind[j] -= 1
                if ind[j] == 0:
                    queue.append(j)
        return count == numCourses


