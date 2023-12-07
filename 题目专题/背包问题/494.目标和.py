#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
# 每个元素都必须使用：找一个正子集和一个负子集使得差值为target
# 即寻找子集总和为(sum+target)/2的个数
# sum+target必须为偶数且大于0，否则没有结果
# 仍旧是01背包问题，但是这里和416不同的是dp之间是有关系的
# 416是传递true，这里是传递方案数量
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if (s+target)%2 or s+target<0:
            return 0
        N = (s+target)//2
        dp = [0]*(N+1)
        dp[0] = 1
        for i in nums:
            for j in range(N,i-1,-1):
                dp[j] = dp[j] + dp[j-i]
        return dp[-1]



# @lc code=end

