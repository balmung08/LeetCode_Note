#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# @lc code=start
'''
# 使用列表实现，列表的in时间需求很长
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = []
        count = max =  0
        for i in range(0,len(s)):
            while s[i] in map:
                map.pop(0)
            map.append(s[i])
            print(map)
            if len(map)>= max:
                max = len(map)
        return max
'''

# 使用带头尾位置指示位的dict代替list，性能更好
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        i = m = 0
        j = -1 # 防止只有一个字符的字符串
        for i in range(0,len(s)):
            if s[i] in map:
                # 下面这一步是为了防止“abba”这样的数据
                # 如果只用map[s[i]]，左边的标志位可能会少1
                j = max(map[s[i]], j)
            map[s[i]] = i
            #print(map)
            if i-j >= m:
                m = i-j
        return m

# @lc code=end

