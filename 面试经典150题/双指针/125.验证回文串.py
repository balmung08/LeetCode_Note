#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
# 双指针
# 也可以正反向分别添加字母，最后进行两个变量的对比
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<=right:
            while not s[left].isalnum() and left<len(s)-1:
                left+=1
            while not s[right].isalnum() and right>0:
                right-=1
            if left>=len(s)-1 or right<=0:
                return True
            if s[left].lower() == s[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True
# @lc code=end

