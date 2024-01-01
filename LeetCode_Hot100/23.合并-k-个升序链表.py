#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
# 按照合并两个链表的思路，依次找最小头合进去
# 通过了，但是耗时非常长，需要优化这个找最小头的步骤
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        Q = P = ListNode(0)
        min = 0
        if lists == []:
            return Q.next
        while True:
            min = 0
            for i in range(len(lists)):
                if lists[min]==None or (lists[i] and lists[i].val<=lists[min].val):
                    min = i
            if lists[min]==None:
                break
            P.next = ListNode(lists[min].val)
            lists[min]=lists[min].next 
            P = P.next
        return Q.next
'''
'''
# 把遍历比较变为放进优先队列
# 确实变快了一个数量级
from queue import PriorityQueue as PQ
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        Q = P = ListNode(0)
        que = PQ()
        res = []
        if lists == []:
            return Q.next
        for i in range(len(lists)):
            if lists[i]:
                que.put([lists[i].val,i])
        while True:
            if que.empty():
                break
            m = que.get()[1]
            if lists[m]:
                P.next = ListNode(lists[m].val)
                P = P.next
                lists[m]=lists[m].next 
                if lists[m]:
                    que.put([lists[m].val,m])
        return Q.next
'''
'''
# 将所有节点全部压入优先队列
# 直接重排
from queue import PriorityQueue as PQ
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        Q = P = ListNode(0)
        que = PQ()
        res = []
        for i in range(len(lists)):
            while lists[i]:
                que.put([lists[i].val,i])
                lists[i] = lists[i].next
        while not que.empty():
            P.next = ListNode(que.get()[0])
            P = P.next
        return Q.next
'''
# 一模一样的思路，但是heapq要快一大截
# heapq没有额外的线程安全验证
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq #调用堆
        minHeap = []
        for listi in lists: 
            while listi:
                heapq.heappush(minHeap, listi.val) #把listi中的数据逐个加到堆中
                listi = listi.next
        dummy = ListNode(0) #构造虚节点
        p = dummy
        while minHeap:
            p.next = ListNode(heapq.heappop(minHeap)) #依次弹出最小堆的数据
            p = p.next
        return dummy.next 


# @lc code=end

