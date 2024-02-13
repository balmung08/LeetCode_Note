#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0 
        n = len(intervals)
        res = []
        # 找左边重合区域
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        tmp = [newInterval[0], newInterval[1]]
        # 找右边重合区域
        while i < n and newInterval[1] >= intervals[i][0]:
            tmp[0] = min(tmp[0], intervals[i][0])
            tmp[1] = max(tmp[1], intervals[i][1])
            i += 1
        res.append(tmp)
        while i < n :
            res.append(intervals[i])
            i += 1
        return res

# @lc code=end

