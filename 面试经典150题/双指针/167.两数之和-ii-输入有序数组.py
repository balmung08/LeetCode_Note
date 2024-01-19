#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
'''
# 结果正确，但是要超时
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = 1
        while start<=len(numbers)-2:
            if end>len(numbers)-1 or numbers[start]+numbers[end]>target:
                start+=1
                end = start+1
            elif numbers[start]+numbers[end]<target:
                end+=1
            elif numbers[start]+numbers[end]==target:
                return [start+1,end+1]
'''
# 在上述双指针方法的基础上改为倒序，头尾双指针从同向变为反向
# 不考虑重复性，没有遍历所有情况
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while start<=len(numbers)-2:
            if end<start or numbers[start]+numbers[end]>target:
                end-=1
            elif numbers[start]+numbers[end]<target:
                start+=1
            elif numbers[start]+numbers[end]==target:
                return [start+1,end+1]

# @lc code=end

