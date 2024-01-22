#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        res = []
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                if i-1==start:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start])+"->"+str(nums[i-1]))
                start=i
        if start==len(nums)-1:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start])+"->"+str(nums[-1]))
        return res
'''
# 为了避免最后一个数字需要单独判断，可以给数组最后加一个非常大的值
# 因为结算不到当前值
class Solution:
    def summaryRanges(self, nums):
        nums.append(2 ** 32)
        ret, start = [], 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if i - 1 == start:
                    ret.append(str(nums[start]))
                else:
                    ret.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        return ret

# @lc code=end

