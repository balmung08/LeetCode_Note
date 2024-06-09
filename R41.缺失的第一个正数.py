#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
# 时间复杂度为n说明不能使用任何排序算法
# 先遍历找最大的数，再构筑set的思路会爆内存
# 原地哈希经典例题
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        L = len(nums)
        for i in range(L):
            # 把当前位置的新数据送到正确的位置
            # 但是换过来的数据不一定对，就换到直到目前的位置数据对了位置
            # 或者当前的数据不在范围内，就没有正确的数据，跳出
            # 如果有重复的数字，也停止交换，不然会卡死
            while 1 <= nums[i] <= L and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # print(i,nums)
        for i in range(L):
            if nums[i] != i+1:
                return i+1
        return L+1
                

        
        
# @lc code=end

