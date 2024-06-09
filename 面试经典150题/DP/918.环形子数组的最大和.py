#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
# 两种情况：正常的和利用到了上/下一次列表的
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1],0)+nums[i]
        dp2 = [0]*len(nums)
        dp2[0] = nums[0]
        for i in range(1,len(nums)):
            dp2[i] = min(dp2[i-1],0)+nums[i]
        if min(dp2) == sum(nums):
            return max(dp)
        else:
            return max(max(dp),sum(nums)-min(dp2))
# @lc code=end

