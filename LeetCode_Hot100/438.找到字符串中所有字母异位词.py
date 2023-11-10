#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
'''
# 这也能超时啊，好好好
# 复杂度n*(k^2)
# 可能是切片的时间与每次tmp2归零的时间导致超时
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        tmp1 = [0] * 26
        result = []
        length = len(p)
        for n in p:
            tmp1[ord(n)-ord('a')] += 1 
        for i in range(0,len(s)):
            tmp2 = [0] * 26
            for j in s[i:i+length]:
                tmp2[ord(j)-ord('a')] += 1 
            if tmp1 == tmp2:
                result.append(i)
        return result
'''
# 用头尾双指针优化掉切片操作
# 这双指针移动和滑动窗口其实本质上是一个思路
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        tmp1 = [0] * 26
        tmp2 = [0] * 26
        result = []
        length = len(p)
        left = 0
        for n in p:
            tmp1[ord(n)-ord('a')] += 1 
            
        for right in range(0,len(s)):
            tmp2[ord(s[right])-ord('a')] += 1 
            # 当加进去的这一位出现冗余时，说明这一位已经不是异位词的一部分
            # 把左边吐出来直到正好符合上
            while tmp2[ord(s[right])-ord('a')] > tmp1[ord(s[right])-ord('a')]:
                tmp2[ord(s[left])-ord('a')] -= 1
                left += 1
            # 当位数一致时就把这一段的头部加入答案中
            if right - left + 1 == length:
                result.append(left)
        return result
# @lc code=end

