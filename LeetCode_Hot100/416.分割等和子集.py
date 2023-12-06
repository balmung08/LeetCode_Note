#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
'''
# 排序双指针这种方法在列表有重复数据的情况下无法使用
# 如[2,2,1,1]
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        start = 0
        end = len(nums)
        while end>start:
            if sum(nums[0:start])>=sum(nums[end:len(nums)]):
                end-=1
            else:
                start+=1
        return sum(nums[0:start])==sum(nums[end:len(nums)])
'''
# 0-1背包问题的通用解法
# 抽象出来的背包价值是总和的一半
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = sum(nums)//2
        if sum(nums)%2:
            return False
        dp = [False]*(N+1)
        dp[0] = True
        for i in nums:
            for j in range(N,i-1,-1):
                dp[j] = dp[j] or dp[j-i]
        return dp[-1]

        
        
# @lc code=end

