#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
'''
# 我们认为目前的子序列其最后一个元素结尾，如果不这么写状态转移方程会很麻烦
# 目前的子序列是前面所有位置可能的新子序列里最长的一个
# 如果dp比之前某个子序列的最后一个值大，那么下面的max里就包括这个子序列
# dp[i] = max(dp[1]……dp[i-1])+1
# 所有子序列里取最大值作为结果
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = 1
        for i in range(1,n):
            dp[i] = 1
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
'''
# 单调栈+二分查找法
# https://leetcode.cn/problems/longest-increasing-subsequence/solutions/922486/xun-xu-jian-jin-dan-diao-zhan-er-fen-cha-d3hf/
# 如果新元素比原本的栈顶大，直接入栈
# 如果新元素比原本的栈顶小，二分找到第一个比栈顶大的元素替换掉
# 维持一个递增单调栈，其长度就是结果
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res

# @lc code=end

