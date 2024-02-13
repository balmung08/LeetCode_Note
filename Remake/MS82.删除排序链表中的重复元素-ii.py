#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        P = ListNode(-101)
        P.next = head
        tmp = P
        last_val = -101
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if tmp.next == head:
                tmp = tmp.next
            else:
                tmp.next = head.next
            head = head.next
        return P.next
# @lc code=end

