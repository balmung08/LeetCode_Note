#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
'''
什么样的数才是一个连续序列的起点？
答案是这个数的前一个数不存在于数组中
因为我们需要能够快速判断当前数num的前一个数num - 1是否存在于数组中

同时当我们定位到起点后，我们就要遍历这个连续序列，什么时候是终点呢？
答案是当前数num的后一个数nunm+1不存在于数组中
因此我们需要能够快速判断当前数num的后一个数num + 1是否存在于数组中
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
        	# 判断是否是第一个数字
            if num - 1 not in nums:
                tmp = 1
                while num + 1 in nums:
                    num += 1
                    tmp += 1
                res = max(res, tmp)
        return res

# @lc code=end

