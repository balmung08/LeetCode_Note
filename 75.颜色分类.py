#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start

'''
# 套用283移动0的思路，遍历两趟，分别把0和1排好
# 这里相当于把要排的删了，计数后在应该补的地方按计数补
# 其实思路做复杂了，但是复杂度倒是差不多
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        fast = slow = count = 0
        fin =  len(nums)
        while fast<=fin-1:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(fast-slow):
            nums.pop()
            nums.insert(0,0)

        fast1 = slow1 = fast-slow 
        while fast1<=fin-1:
            if nums[fast1] != 1:
                nums[slow1] = nums[fast1]
                slow1 += 1
            fast1 += 1
        for i in range(fast1-slow1):
            nums.pop()
            nums.insert(fast-slow,1)
'''
# 其实一趟循环也能完事，遇到0删了填到头部，遇到2删了填到尾部
# 没必要再用另外两个指针来记0和2段的位置了
# 性能和上边那个也差不多，复杂度都是n
# 但是如果不止三种，那么还是需要按顺序一种一种排
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = 0
        count2 = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0,0)
            if nums[i] == 2:
                nums.pop(i)
                count2 += 1
                i -= 1
            i += 1
        for i in range(count2):
            nums.append(2)
        
                


        
# @lc code=end

