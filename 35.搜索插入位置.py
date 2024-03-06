#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
# 标准二分查找模板
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
        while last >= first:
            if nums[(last+first)//2]>=target:
                last = (last+first)//2-1
            elif nums[(last+first)//2]<target:
                first = (last+first)//2+1
        return first

# @lc code=end

