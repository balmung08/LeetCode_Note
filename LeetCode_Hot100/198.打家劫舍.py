#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
'''
# 二维DP
# 目前房间不偷：dp[i][0] = max(dp[i-1][0],dp[i-1][1])
# 目前房间偷：dp[i][1] = dp[i-1][0]+price
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for i in range(2)] for j in range(n+1)]
        dp[1][0] = 0
        dp[1][1] = nums[0]
        for i in range(1,n+1):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            dp[i][1] = dp[i-1][0]+nums[i-1]
        return max(dp[-1][0],dp[-1][1])
'''
'''
# 一维DP
# 偷第n间的情况即前n-2间屋子能抢到的最大金额加上第n间屋子金额
# 不偷第n间的情况即前n-1间屋子能抢到的最大金额
# f(k) = max{ rob(k-1), nums[k-1] + rob(k-2) }
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        N = len(nums)
        dp = [0] * (N+1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, N+1):
            dp[k] = max(dp[k-1], nums[k-1] + dp[k-2])
        return dp[N]
'''
# 状态压缩空间优化：
# 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
# 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        for i in nums:
            prev, curr = curr, max(curr, prev + i)
        return curr
# @lc code=end

