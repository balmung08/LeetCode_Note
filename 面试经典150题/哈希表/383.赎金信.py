#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
'''
# 哈希表记录与判断
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        w_d = {}
        for i in magazine:
            if not i in w_d:
                w_d[i] = 1
            else:
                w_d[i]+=1
        for i in ransomNote:
            if i in w_d:
                w_d[i]-=1
                if w_d[i]<0:
                    return False
            else:
                return False
        return True
'''

# python的count函数计数
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        List = []
        for i in ransomNote:
            if i not in List:
                List.append(i)
                if ransomNote.count(i) > magazine.count(i):
                    return False
        return True


# @lc code=end

