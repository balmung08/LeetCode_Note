#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
'''
# 先排序再倒着找
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        res = 0
        for i in range(len(citations)-1,-1,-1):
            if citations[i]>res:
                res+=1
        return res
'''
# 计数加求和
# 使用一个额外的数组存储每个引用次数
# 还是得倒着找，但是遍历的复杂度n比排序的nlogn小
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        res = 0
        nums = [0]*(n+1)
        for i in citations:
            nums[min(i,n)]+=1
        for i in range(n, -1, -1):
            res += nums[i]
            if res>=i:
                return i

# @lc code=end

