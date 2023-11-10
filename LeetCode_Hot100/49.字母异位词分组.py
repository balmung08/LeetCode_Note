#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
'''
# 哈希表
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hash = {}
        # 采用哈希表判断是否是异位词
        for i in strs:
            tmp = [0] * 26
            for j in i:
                tmp[ord(j)-ord('a')] += 1 # 关键语句，以'a'为基点来计数
            if Hash.get(tuple(tmp)) is None:
                Hash[tuple(tmp)] = [i]
            else:
                Hash[tuple(tmp)].append(i)
                
        return list(Hash.values())
'''

# 通过异位词进行排序来保证key的唯一性
# 理论上哈希表应该更快一点，可能是此题数据给的数量多长度短造成这个排序反而更快了
# 不过不知道tuple转换函数的复杂度，也可能是差在这了
# 下面这个思路上更直接一些
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            
            # 如果该键已经在字典中，将当前单词加入到对应的列表中
            if sorted_word in dic:
                dic[sorted_word].append(i)
            else:
                dic[sorted_word] = [i]
        return list(dic.values())

# @lc code=end

