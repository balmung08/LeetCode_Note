#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 组翻转思路
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(left, right):
            pre, cur = left, left.next
            first, last = pre, cur
            while cur != right:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                first.next = pre
            last.next = right
            return last

        C = ListNode(0)
        C.next = head
        start = C
        tail = head
        cnt = 0
        while tail:
            cnt += 1
            tail = tail.next
            if cnt % k == 0:
                start = reverse(start, tail)
        return C.next

# @lc code=end

