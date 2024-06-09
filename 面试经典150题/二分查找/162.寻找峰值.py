#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
# 根据时间复杂度要求肯定不能遍历而是需要使用二分
# 如果中间数比其右边大则说明左边一定有一个峰值，比其左边大就一定右边有峰值
# 其实可以根据导数的思路来想
# 题目给出了相邻数不会相等的条件
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        first = 0
        last = len(nums)-1
        while last > first:
            if nums[(last+first)//2]>=nums[(last+first)//2+1]:
                last = (last+first)//2
            else:
                first = (last+first)//2+1
        return first
# @lc code=end

