#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0,n+1):
            i = bin(i)
            res.append(i.count("1"))
        return res
# @lc code=end

