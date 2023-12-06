#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
'''
# @lc code=start
# 使用完全背包问题类似的思路
# 对词组能否组成词语从0开始依次拼起来
# 结果减去worddict里所有比自己短的词组后
# 只要有一个减去后的结果在以前被拼起来过
# 这个词组就可以被拼起来，直接break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        M = len(wordDict)
        dp = [False]*(N+1)
        dp[0] = True
        for i in range(1,N+1):
            for j in [n for n in wordDict if len(n)<=i]:
                if s[i-len(j):i] == j and dp[i-len(j)]==True:
                    dp[i] = True
                    break
        return dp[-1]
'''   
# 完全背包问题的通用模板
class Solution(object):
    def wordBreak(self, s, wordDict):
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j]=True 
        return dp[-1]


# @lc code=end

