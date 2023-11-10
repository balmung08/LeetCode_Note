#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
# @lc code=start
'''
# 数据有负数，因此不能使用滑动窗口
# 暴力法就不写了，最低也是n^2
# 前缀和法的list暴力遍历也会超时，这样也是n^2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        sum = [0]
        s = 0
        for i in nums:
            s += i
            sum.append(s)
        for n in range(0,len(nums)+1):
            for m in range(n+1,len(nums)+1):
                if sum[m]-sum[n] == k:
                    result += 1
        return result
'''
# 一边计算前缀和的时候一边就把次数给计了
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # key 为累加值 acc，value 为累加值 acc 出现的次数
        d = {}
        acc = count = 0
        for num in nums:
            acc += num
            # 前缀和为k的话直接加一
            if acc == k:
                count += 1
            # 当前位置前缀和减去之前某一位的前缀和等于目标值
            # 把存在次数加进去
            if acc - k in d:
                count += d[acc-k]
            # 如果前缀和与之前的某个情况相同，存在次数加一
            if acc in d:
                d[acc] += 1
            # 否则新建一种前缀和情况
            else:
                d[acc] = 1
        return count
# @lc code=end

