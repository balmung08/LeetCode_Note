#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
'''
# 前缀和加滑窗
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        res,tmp = 0,0
        sum_d = [0]
        for i in nums:
            tmp+=i
            sum_d.append(tmp)
        while right<=len(nums)-1:
            while sum_d[right]-sum_d[left]<target:
                right+=1
                if right==len(nums):
                    break
            while sum_d[right]-sum_d[left]>=target:
                if res == 0:
                    res = right-left
                else:
                    res = min(res,right-left)
                left+=1
        return res
'''
# 可以直接滑窗，不需要前缀和
# 滑动思路与上面一样的
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums : return 0
        left = 0
        cur = 0
        res = float("inf")
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return res if res != float("inf") else 0

# 前缀和加二分查找
# 在前缀和数组下标 [0,i][0, i][0,i] 范围内找到满足「值小于等于 s−ts - ts−t」的最大下标，充当子数组左端点的前一个值。
# 会慢很多，是nlogn，上面滑窗是n
class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:
        n, ans = len(nums), len(nums) + 10
        s = [0] * (n + 10)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            d = s[i] - t
            l, r = 0, i
            while l < r:
                mid = (l + r + 1) // 2
                if s[mid] <= d:
                    l = mid
                else:
                    r = mid - 1
            if s[r] <= d: 
                ans = min(ans, i - r)
        return 0 if ans == n + 10 else ans


# @lc code=end

