#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# 拉到列表里反转重新赋值
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0,head)
        L = []
        R = result = ListNode(0)
        while head:
            L.append(head.val)
            head = head.next
        L.reverse()
        for i in L:
            result.next = ListNode(i)
            result = result.next
        return R.next
'''
# 节点依次反转
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        space = None
        while head:
            tmp = head.next
            head.next = space
            space = head
            head = tmp
        return space


# @lc code=end

