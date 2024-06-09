#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
# 不可能列表实时排序
# 优先队列又不能按照index访问，无法直接获取中间的值
#（实际上python是可以的，但是过于取巧）
# 因此采用两个堆，一个大顶堆一个小顶堆，从中间断开
# 两个堆顶就是中位数
# heapq没有大顶堆，只能把数据取反了塞进去
# 假设数据为奇数，此时我们设定希望小顶堆总比大顶堆多一个
# 此时小顶堆的值弹出来就是中位数，否则两个堆顶弹出除以2
# 小顶堆存的是中位数大的那边，大顶堆存的是中位数小的那边
from heapq import *
class MedianFinder:
    def __init__(self):
        self.heap_small = []
        self.heap_large = []

    def addNum(self, num: int) -> None:
        if len(self.heap_large) != len(self.heap_small):
            # 长度不同，此时大顶堆长度需要+1
            # 因此先往小顶堆里塞，再弹到大顶堆里
            heappush(self.heap_small,num)
            heappush(self.heap_large,-heappop(self.heap_small))
        else:
            # 先往大顶堆里塞，如果他不属于这边
            # 会被弹出来再塞到小顶堆那边，此时小顶堆确实也多一个
            heappush(self.heap_large, -num)
            heappush(self.heap_small, -heappop(self.heap_large))

    def findMedian(self) -> float:
        if len(self.heap_large) == len(self.heap_small):
            return (self.heap_small[0]-self.heap_large[0])/2
        else:
            return self.heap_small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

