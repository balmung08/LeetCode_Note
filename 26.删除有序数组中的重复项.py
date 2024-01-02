#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        left=1
        right=1
        while right<len(nums) and nums[left]!=nums[left-1]:
            left+=1
            right+=1
        while right<len(nums):
            while right<len(nums)-1 and nums[right]==nums[right+1]:
                right+=1
            if nums[right]>nums[left]:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            # print(nums,left,right)
            right+=1
        return left
'''
# 不交换只赋值
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast + 1
        return slow + 1

# [1,2]
# @lc code=end

