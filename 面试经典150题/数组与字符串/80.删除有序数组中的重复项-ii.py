#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 变动1: 由于元素可以重复2次，left现在从第二个元素开始，right从第三个元素开始
        slow, fast = 1,2
        while fast < len(nums):
            # 变动2: 以前之和nums[left]比, 现在还要和nums[left - 1]比，从而保证元素可以重复两次
            if nums[fast] != nums[slow] or nums[fast] != nums[slow - 1]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+ 1


# @lc code=end

