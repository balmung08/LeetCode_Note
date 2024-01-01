#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start

# 头尾双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            if nums[left] == val:
                nums[left],nums[right] = nums[right],nums[left]
                right -= 1
            else:
                left += 1
        return left

# 头尾双指针的优化：在一个循环里做更多的事情
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            while nums[right]==val:
                if right == left:
                    return left
                right -= 1
            if nums[left] == val:
                nums[left],nums[right] = nums[right],nums[left]
                right -= 1
            left += 1
        return left
'''

# [0,1,2,2,3,0,4,2]\n2
# [1]\n1
# [2,2,3]\n2

# @lc code=end

