#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
# # 要重新看！
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         # 切到第i位，后面的进行递归，前面的原封不动加上后边生成的结果
#         def backtrace(s):
#             path = []
#             if not s:
#                 return [[]]
#             if len(s) == 1:
#                 return [[s]]
#             for i in range(1,len(s)+1):
#                 if s[:i][::-1] == s[:i]:
#                     # 注意此处数据的格式
#                     path += [[s[:i]]+j for j in backtrace(s[i:])]
#             return path
#         return backtrace(s)

# DP
# 新的所有的回文串组相比前一次所有的回文串组有且只有三种情况
# 1 直接在回文串组后添加新的字符
# 2 回文串组的最后一项为单字符且与新的字符相同
# 3 回文串组拥有两项以上且倒数第二串与新的字符相同

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == "":
            return []
        ans = [[s[0]]]
        for i in range(1, len(s)):
            curr = s[i]
            newAns = []
            for item in ans:
                newAns.append(item + [curr])
                if item[-1] == curr:
                    newAns.append(item[0:-1] + [item[-1] + curr])
                if len(item) >= 2 and item[-2] == curr:
                    newAns.append(item[0:-2] + [item[-2] + item[-1] + curr])
            ans = newAns 
        return ans

            

# @lc code=end

