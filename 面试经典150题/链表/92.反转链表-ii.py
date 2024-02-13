#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# 分段翻转+插入
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        P = ListNode(0)
        Q = P
        P.next = head
        for i in range(left-1):
            P = P.next 
        M = P
        P = P.next
        space = None
        for j in range(right-left+1):
            tmp = P.next
            P.next = space
            space = P
            P = tmp
        # 此时实际上第一段末尾是接着翻转后第二段末尾的
        # 先把第二段末尾和第三段接上，再接第一段末尾和第二段开头
        # print(M.val,M.next.val)
        M.next.next = P
        M.next = space
        # 不能返回head，因为head也可能是需要翻转的，只能返回哨兵节点的下一个
        return Q.next
'''
# 多指针插入
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        # 找到翻转链表部分的前一个节点, 1->2->3->4->5->NULL, m = 2, n = 4 指的是 节点值为1
        for _ in range(m - 1):
            pre = pre.next
        # 用 pre, start, tail三指针实现插入操作
        # tail 是插入pre,与pre.next的节点
        start = pre.next
        tail = start.next
        for _ in range(n - m):
            start.next = tail.next
            tail.next = pre.next
            pre.next = tail
            tail = start.next
        return dummy.next

