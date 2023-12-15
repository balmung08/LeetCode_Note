#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
'''
# 首先上DP，超时了
# 回溯只会比DP更慢
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[0] = True
        for i in range(0,len(nums)):
            if dp[i]:
                for j in range(0,min(nums[i]+1,len(nums)-i)):
                    dp[i+j] = True
        return dp[-1]
'''
# 必须使用贪心算法
# 遍历每个位置可以到达的最远距离，看是否能够到达最后
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
        
# @lc code=end

