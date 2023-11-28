#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
# 子数组需要满足的条件：
# 1.前后的其他数组均为升序排列
# 2.前面的最后一个数小于子数组内最小值，后面第一个数大于子数组内最大值
# 可以简化为找到比升序数列的最大值小的第一个值为左界
# 倒着找，比倒序数列最小值大的第一个值为右界
# --------------------------
# 先找不为升序序列的两个节点
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        max_num=nums[0]
        right=0
        # 找右节点
        for i in range(n):
            if(nums[i]>=max_num):
                max_num=nums[i]
            else:
                right=i
        # 找左节点
        left=n
        min_num=nums[-1]
        for i in range(n-1,-1,-1):
            if(nums[i]<=min_num):
                min_num=nums[i]
            else:
                left=i
        return right-left+1 if(right-left+1 >0) else 0
# @lc code=end

