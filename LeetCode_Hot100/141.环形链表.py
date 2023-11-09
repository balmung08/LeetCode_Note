#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 如果有环，快指针会绕回来追到慢指针
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        count = 0
        while fast:
            fast = fast.next.next if fast.next is not None else fast.next
            slow = slow.next
            count += 1
            if fast == slow and count != 1:
                return True
        return False
# @lc code=end

