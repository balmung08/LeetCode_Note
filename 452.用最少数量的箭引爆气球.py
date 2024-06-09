#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
# 找一个数处于最多的区间内
# 找交集数量（合并区间是找并集数量）
# 和LC56"合并区间"一起比对
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = []
        # print(points)
        for i in points:
            if res == [] or i[0]>res[-1][1]:
                res.append(i)
            else:
                res[-1][0] = max(i[0],res[-1][0])
                res[-1][1] = min(i[1],res[-1][1])
            # print(res)
        return len(res)
# @lc code=end

