#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
# 二维DP
# 非常漂亮的状态抽象和状态转移
# 真想不出来，直接开背

# dp[i][j]代表word1中前i个字符变换到word2中前j个字符，最短需要的操作数
# 在单词 A 中插入一个字符：
# 如果我们知道 horse 到 ro 的编辑距离为 a，
# 那么显然 horse 到 ros 的编辑距离不会超过 a + 1。

# 在单词 B 中插入一个字符：
# 如果我们知道 hors 到 ros 的编辑距离为 b，
# 那么显然 horse 到 ros 的编辑距离不会超过 b + 1

# 修改单词 A 的一个字符：
# 如果我们知道 hors 到 ro 的编辑距离为 c，
# 那么显然 horse 到 ros 的编辑距离不会超过 c + 1
# 因为前面变好以后最后一个字母不相同的话，直接改变即可

# 如果刚好最后两个字母相同，那么可以直接参考dp[i-1][j-1]，操作不用加一
# 因为本质上只需要修改前面几个字符，最后一个字符不起作用

# 官解写的很好
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        # 初始化
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(n + 1):
            dp[0][i] = i
        # 状态转移
        # i , j 代表 word1, word2 对应位置的 index
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果word1[:i][-1]==word2[:j][-1]
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 否则从三种状态中选一个最小的然后 +1
                else:
                    dp[i][j]=min(dp[i-1][j-1], min(dp[i-1][j],dp[i][j-1]))+1
        return dp[m][n]
# @lc code=end

