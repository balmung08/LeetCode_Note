#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrace(i,res):
            print(i,res)
            if len(res) >= k:
                ans.append(res)
                return
            else:
                for a in range(i,n+1):
                    backtrace(a+1,res+[a])
        backtrace(1,[])
        return ans
# @lc code=end

