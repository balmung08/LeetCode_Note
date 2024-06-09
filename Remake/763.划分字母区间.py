#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
# 首先遍历一遍，获取所有元素最后出现的位置
# 贪心算法：获取当前字符串中从开头为止使得同一字符的开始与结尾全部包含的子串
# 因此，需要不停检查左指针对应的字符的最后位置是否在右指针范围内
# 如果不在，右指针需要移到对应位置
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        right = 0
        hash_map = defaultdict()
        for i in range(len(s)):
            hash_map[s[i]] = i
        res = []
        # 使每一段尽可能长
        while right < len(s):
            while right>=left:
                if hash_map[s[left]]>right:
                    right = hash_map[s[left]]
                left+=1
            left = right
            right += 1
            if res: res.append(right-sum(res))
            else: res.append(right)
        return res

# @lc code=end

