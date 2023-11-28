#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
'''
# 使用python的字典排序函数直接完成排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        res = []
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        new = sorted(dict.items(),  key=lambda d: d[1], reverse=True)
        for i in range(0,k):
            res.append(new[i][0])
        return res
'''
# 搓一个小顶堆，把字典的键丢进去，按照值进行优先队列排序再弹出k个也可以
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        heap_max = []
        dic_fre = {}
        ans = []
        for i in nums:
            if i in dic_fre:
                dic_fre[i]+=1
            else:
                dic_fre[i] = 1
        # 最好是只维护堆的长度为k，实时弹出多余的元素
        # 但是这里没写
        for i in dic_fre:
            heapq.heappush(heap_max,(-dic_fre[i],i))
        for j in range(k):
            p = heapq.heappop(heap_max)
            ans.append(p[1])
        return ans
# @lc code=end

