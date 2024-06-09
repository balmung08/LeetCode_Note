#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Q = p = ListNode(0)
        Q.next = p
        p.next = P = head
        if p == None:
            return None
        while p.next and p.next.next:
            M = p.next
            L = p.next.next
            N = p.next.next.next
            p.next = L
            p.next.next = M
            p.next.next.next = N
            p = p.next.next
            # 可简化为如下代码
            # temp.next = node2
            # node1.next = node2.next
            # node2.next = node1
        return Q.next
# @lc code=end

