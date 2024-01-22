#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
'''
# 双指针比较仅头尾是不行的，可能尾巴会和中间某个数有重合
# 需要使用一个表记录头尾之间的所有数据
# 即维护一个长度为k的滑窗
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hash_set = set()
        i = 0
        for i in range(n):
            if nums[i] in hash_set:
                return True
            hash_set.add(nums[i])
            if len(hash_set) == k+1:
                hash_set.remove(nums[i-k])
        return False
'''
# 或者纯哈希表找以前是否出现过目前的数字
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False

# @lc code=end

