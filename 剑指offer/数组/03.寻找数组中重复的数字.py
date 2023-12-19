# 字典检查重复
'''
class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        dict = {}
        for i in documents:
            if i in dict:
                return i
            dict[i] = 1
'''
# 不占额外空间，数组原地排序
class Solution:
    def findRepeatDocument(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        n = len(nums)
        for index in range(1, n):
            if pre == nums[index]:
                return pre
            pre = nums[index]