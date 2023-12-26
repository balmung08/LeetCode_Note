#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            # 使用库完成最小顶堆
            heapq.heappush(heap, num)
            if len(heap) > k:
                # 弹出最小项
                heapq.heappop(heap)
        return heapq.heappop(heap)

# @lc code=end

