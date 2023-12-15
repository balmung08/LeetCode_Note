#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
# 在排序以后，res里的每个数据都比要插入的数据高
# 因此只需要考虑每一个元素应该在的位置，局部最优在排好序的情况下就是全局最优
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key=(lambda x:[-x[0],x[1]]))
        for i in people:
            if i[1] > len(res)-1:
                res.append(i)
            else:
                res.insert(i[1],i)
        return res

# @lc code=end

