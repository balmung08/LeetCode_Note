#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        for i in range(numRows-1):
            step = []
            step.append(1)
            for j in range(len(res[-1])-1):
                step.append(res[-1][j]+res[-1][j+1])
            step.append(1)
            res.append(step)
        return res


# @lc code=end

