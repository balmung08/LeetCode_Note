#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        count = 0
        for i in bin(x^y):
            if str(i) == str(1):
                count += 1
        return count
        '''
        # 这个和上面那个性能差不太多，可能好一点
        # 基本上最优解也就这样，懒得刷了
        print(bin(x).type())
        return bin(x^y).count('1')
# @lc code=endb

