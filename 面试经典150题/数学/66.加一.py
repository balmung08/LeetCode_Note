#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        s = 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+s<10:
                res.append(digits[i]+s)
                s = 0
            else:
                res.append(digits[i]+s-10)
                s = 1
        if s == 1:
            res.append(1)
        res.reverse()
        return res
# @lc code=end

