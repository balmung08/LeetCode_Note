#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#

# @lc code=start
'''
# 粗暴的优先队列方法会爆内存
from queue import PriorityQueue
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = PriorityQueue()
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                q.put((nums1[i]+nums2[j], [nums1[i],nums2[j]]))
        for n in range(k):
            res.append(q.get()[1])
        return res
'''

# 注意出入堆思路以及针对0的特殊处理
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        h = [(nums1[0] + nums2[0], 0, 0)]
        while h and len(ans) < k:
            _, i, j = heappop(h)
            ans.append([nums1[i], nums2[j]])
            if j == 0 and i + 1 < len(nums1):
                heappush(h, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans



# @lc code=end

