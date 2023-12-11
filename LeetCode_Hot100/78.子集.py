#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
'''
# 在原本的集合上删去元素
import copy
class Solution:
    def __init__(self) -> None:
        self.res = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        def dfs(n,path):
            if len(path) == 0:
                 return None
            for i in range(n,l):
                d = copy.deepcopy(path)
                if nums[i] in d:
                    self.res.append(d)
                    d.remove(nums[i])
                else:
                    return None 
                dfs(n+1,d)
        dfs(0,nums)
        self.res.append(nums)
        return self.res
# 123 23 3 2 13 1 12 
'''
# 在原本的集合上拼接元素
# i表示目前已经加过的元素
# 1 12 123 13 2 23 3 
class Solution:
    def __init__(self) -> None:
        self.res = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(n,path):
            if n == len(nums):
                self.res.append(path)
                return None
            self.res.append(path)
            for i in range(n,len(nums)):
                dfs(i+1,path+[nums[i]])
        dfs(0,[])
        return self.res

# @lc code=end

