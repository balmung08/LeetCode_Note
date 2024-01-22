#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
# 最多就十位整数，一次就能跳进810以内
# 如果是快乐数，一定会收敛于1
# 如果不是，会出现环
class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        visited = set()
        while True:
            n = str(sum(int(i) ** 2 for i in n))
            if n == "1":
                return True
            if n in visited:
                return False
            visited.add(n)
    
# @lc code=end

