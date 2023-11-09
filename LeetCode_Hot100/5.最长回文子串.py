#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
'''
# 双循环暴力遍历，过是能过但是巨慢
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        result = ""
        for i in range(0,len(s)+1):
            for n in range(i+1,len(s)+1):
                part = s[i:n]
                if part == part[::-1]:
                    if length<= len(part):
                        length = len(part)
                        result = part
        return result
'''
'''
# 中心扩散法Spread From Center
# 给出每个字符可扩散的最长回文串
def spread(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s如果本身全是回文串就直接返回
        if s==s[::-1]:
            return s
        res = s[:1] # s是首个字符组成的字符串，存储上一次的最长
        for i in range(len(s)):
            palindrome_odd= spread(s,i, i)
            # 应对像"cbbd"这样的偶数个数据，使左右两边不对称
            palindrome_even= spread(s,i, i + 1)
            # 当前找到的最长回文子串
            res = max(palindrome_odd,palindrome_even,res,key=len)
        return res

'''
# 动态规划法
# 在这题里慢的一逼，虽然还是比暴力快点
# 这里的动态规划实际上只有检测字符串是否是回文的时候，因此对性能提升很小
# 利用了子字符串是否是回文的结论来优化判断字符串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        # 二维dp记忆表
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

# 其实最快的是马拉车算法，不过好像也只能判断回文，没啥别的用
# @lc code=end

