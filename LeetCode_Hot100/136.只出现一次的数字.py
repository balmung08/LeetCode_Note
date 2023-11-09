#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
'''
# 单纯使用哈希表存储满足了时间复杂度,但是空间复杂度为n
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        space = set()
        for i in nums:
            if not i in space:
                space.add(i)
            else: 
                space.remove(i)
        for i in space:
            return i
'''     
# 用排序也可以，但是时间复杂度和空间复杂度总有一个超了
# 位操作   
# 位运算具有交换律，两个相同的数做异或结果为0，而0和0的异或为0，最后全是0
# 唯一不为0的数和0做位异或，结果不变
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result

        
        

# @lc code=end

