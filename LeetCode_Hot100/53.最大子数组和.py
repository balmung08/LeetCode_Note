#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
# 计算每个长度的字符串的可能最大值
# 如果前面的总和大于0，则目前的可能最大值就是之前的加现在的
# 如果前面总和小于0，则目前的可能最大值就是从现在开始，不算上之前的了
# 因为必须连续，因此不存在最大值中断的现象
# 带上目前项的一定和前一项强相关
# dp结果可能会变小也是由于这个性质：走过了以后数组就不连续了
# 因此最后还需要增加一个步骤，即在dp列表里找最大值
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(0,dp[i-1])+nums[i]
        return max(dp)

# @lc code=end

