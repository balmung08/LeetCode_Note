#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        def dfs(n,path):
            if n == len(nums):
                self.res.append(path)
                return None
            else:
                for i in range(0,len(path)+1):
                    dfs(n+1,path[:i]+[nums[n]]+path[i:])
        dfs(0,path)
        return self.res
# @lc code=end

