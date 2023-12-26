# 使用三个指针分别表示三个因数的组成个数
# https://leetcode.cn/problems/chou-shu-lcof/solutions/263122/chou-shu-ii-qing-xi-de-tui-dao-si-lu-by-mrsate/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]*n
        a = b = c = 0
        for i in range(1, n):
            dp[i] = min(dp[a]*2 , dp[b]*3 , dp[c]*5)
            if dp[i] == dp[a]*2:a += 1
            if dp[i] == dp[b]*3:b += 1
            if dp[i] == dp[c]*5:c += 1
        return dp[-1]