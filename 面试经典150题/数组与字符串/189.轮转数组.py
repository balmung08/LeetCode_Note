#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
'''
# 删去k的多余周期
# 切片对换方式
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k>len(nums):
            k-=len(nums)
        part1 = nums[len(nums)-k:]
        part2 = nums[:len(nums)-k]
        nums[k:] = part2
        nums[:k] = part1
# 实际上也可以 nums[:] = nums[n - k:] + nums[:n - k]解决
'''
'''
# 辅助空间法
# 和上面的一样也是空间换时间
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k>len(nums):
            k-=len(nums)
        L = len(nums)
        tmp = nums
        nums[:] = tmp + tmp
        nums[:] = nums[L-k:2*L-k]
'''
'''
# 暴力对换，时间很慢
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())
'''


# 还有个环状替换法
# 一直寻找下一个被替换的元素应该去向的位置
class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        cnt = 0
        start = 0
        while cnt < len(nums):
            current = start
            pre = nums[start]
            while True:
                nxt = (current + k) % len(nums)
                nums[nxt], pre = pre, nums[nxt]
                current = nxt
                cnt += 1
                if start == current:
                    break
            start += 1

# 翻转法
# 先全部翻转，再分段翻转
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))
# @lc code=end

