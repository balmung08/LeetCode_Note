#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start   
# 使用dp[i]表示包含第i个括号的最长括号串
# 因此dp[i]一定得以)结尾才能有效
# 如果前一个字符是(，则dp[i] = dp[i-2]+2  
 
# 如果前一个字符是)，有可能是(())这种情况
# 找到前一个字符是(的位置，加上它前面的最长字符串和中间的最长字符串再加2
# dp[i] = dp[i − 1] + dp[i - dp[i - 1] - 2] + 2
class Solution:
    def longestValidParentheses(self, s: str) -> int:  
        if s == "":
            return 0      
        dp = [0]*len(s)
        for i in range(len(s)):
            if s[i] == ")":
                # 避免python负数的从后往前取值
                if i - 1 < 0: 
                    continue
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0 ) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) +2

        return max(dp)

# @lc code=end

