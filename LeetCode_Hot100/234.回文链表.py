#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# 全拉出来看正反相不相等，很简单，但是很慢
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a == a[::-1]
'''

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow,fast,prev = head,head,None
        # 取出后半段
        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else fast.next
        # 反转后半段
        while slow is not None:
            slow.next, slow, prev = prev, slow.next, slow
        # 后半段和原链表比较，原链表不需要切
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
# @lc code=end

