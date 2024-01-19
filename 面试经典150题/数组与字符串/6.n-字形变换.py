#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
# 可以使用推出的公式决定编号
# 也可以使用flag和direction两个变量决定
# 每当flag到达numRows和1时就变向
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        if numRows == 1:
            return s
        for i in range(1, numRows + 1):
            start = i-1
            if i == 1:
                res+=s[0]
            while start <= len(s) - 1:
                if i != 1:
                    res += s[start]
                start += 2 * (numRows - i)
                if start <= len(s) - 1 and numRows != i:
                    res += s[start]
                start += 2 * (i - 1)
        return res

# @lc code=end

