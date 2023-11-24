#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start

# 我不管了，我要用除法，可恶！
# 不用除法，但是把数组遍历放大的过程也是n的复杂度
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        h = []
        res = 1
        for index,value in enumerate(nums):
            if h == []:
                h.append(1)
                res *= value
            else:
                h = [i * value for i in h]
                h.append(res)
                res *= value
        return h
'''
# 正向遍历获取前缀积，反向遍历获取后缀积
# 由于返回数组不计入，则可以看作是常数空间复杂度
# 没有使用额外的表来存储而是实时改变了结果数组
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        k=1
        for i in range(n):
            res[i]=k
            k=k*nums[i]
        k=1
        for i in range(n-1,-1,-1):
            res[i]*=k
            k*=nums[i]
        return res
# @lc code=end

