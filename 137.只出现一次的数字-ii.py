#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
# 可以按照数电逻辑电路的设计方式，先写出表格再找关系
# https://leetcode.cn/problems/single-number-ii/solutions/247652/luo-ji-dian-lu-jiao-du-xiang-xi-fen-xi-gai-ti-si-l/?envType=study-plan-v2&envId=top-interview-150

# 常见解法是统计每一位的1出现次数
# 出现次数能被3整除就是0，否则是1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = sum(num >> i & 1 for num in nums)
            if cnt % 3:
                if i == 31:
                    ans -= 1 << i
                else:
                    ans |= 1 << i
        return ans



# @lc code=end

