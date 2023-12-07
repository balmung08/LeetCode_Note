#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
# 与连续最大和很像，但是负数会影响结果，如[2,-3,-4]
# 如果只用一个数组存最大值，dp会是[2,-3,4]，到-3时-6会被舍去从而失去负负得正机会
# 因此使用两个数组，一个正数最大值，一个存负数绝对值最大值，即最小值
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n)
        dp1 = [0]*(n)
        dp[0]=dp1[0]=nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]*nums[i],nums[i],dp1[i-1]*nums[i])
            dp1[i] = min(dp[i-1]*nums[i],nums[i],dp1[i-1]*nums[i])
        return max(dp)
# @lc code=end

