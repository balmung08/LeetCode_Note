#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
'''
# 用DP的话矩阵里存储的数据不好确定
# 背包问题常规也就是确定个数，如果要存储每个可能的结果，需要使用额外的步骤记录
# 本质上是完全背包问题，主要看这个方法如何去重的
# 完全背包问题的思路会依次使用所有元素，使用前面的元素时与后面的无关
# 可能重复的原因是元素可能有重复，而这个题的所有元素各不相同
# 因此不需要额外去重
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = {i:[] for i in range(target+1)}
        dp[0] = [[]]
        for num in candidates:
            for i in range(num, target+1):
                if dp[i-num]:
                    for a in dp[i-num]:
                        dp[i].append([num]+a)
        return dp[target]
'''
# 回溯法
# 其实所有DP问题都可以使用回溯法，只是DP更快
# 重点在于使用start控制可以被加入的candidate的范围
# 第一轮必定使用了第一个元素且可以使用所有元素
# 第二轮必定使用第二个元素且不能使用第一个元素，以此完成了对第一个元素的去重
class Solution:
    def __init__(self) -> None:
        self.res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        min_v = min(candidates)
        def dfs(n,path,start):
            if n<min_v:
                if n==0:
                    self.res.append(path)
                else:
                    return None
            else:
                for i in range(start,len(candidates)):
                    dfs(n-candidates[i],path+[candidates[i]],i)
        dfs(target,path,0)
        return self.res 
# @lc code=end

