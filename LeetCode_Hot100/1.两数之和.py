#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
'''
# 双循环检测，复杂度n^2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, value1 in  enumerate(nums):
            for index2, value2 in  enumerate(nums):
                if index1 == index2:
                    continue
                if index1 != index2:
                    sum = value1 + value2
                    if sum == target:
                        return [index1,index2]
'''

'''
# 去除了重复循环，但是复杂度仍为n^2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
                    if (target - nums[i]) in nums[i+1:]:
                        j = nums[i+1:].index(target - nums[i])
                        return [i, j + i + 1]
            
'''
# 字典的in时间复杂度是1，比列表查找快很多
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for idx,num in enumerate(nums):
            if target-num not in d:
                d[num]=idx
            else:
                return [idx,d[target-num]]

# @lc code=end

