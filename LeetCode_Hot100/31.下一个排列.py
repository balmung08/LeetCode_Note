#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
# 倒着看数字是否是倒序排列
# 直到非倒序排列的时候就把这个数加进来进行下列操作
# 取比这个数大的最小数填到开头，剩下的升序排列
# 这个数字就是逆序排列的最靠前的一个数字，因此交换顺序即可
# 后面的数字逆序即可
# 如果所有数字都是倒序排列，就直接返回reverse
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pre = None
        position = None
        flag_change = False
        n = len(nums)
        for i in range(n-1,-1,-1):
            if pre == None:
                pre = nums[i]
                continue
            else:
                if nums[i]>=pre:
                    pre = nums[i]
                    continue
                else:
                    position = i
                    flag_change = True
                    break
        if not flag_change:
            nums.reverse()
        else:
            for i in range(n-1,-1,-1):
                if nums[i]>nums[position]:
                    nums[position],nums[i] = nums[i],nums[position]
                    break
            nums[position+1:] = reversed(nums[position+1:])

# [1,2,4,3] - 1324
# [1,2,3]
# @lc code=end

