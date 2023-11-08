#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
# 等比指针获取环的长度
# 等差指针获取头位置
def get_cycle_num(head):
    fast = slow = head
    count = 0
    first = 0
    flag = True
    n = 0
    while fast:
        fast = fast.next.next if fast.next is not None else fast.next
        slow = slow.next
        count += 1
        if fast == slow and count != 1 and flag == True:
            flag = False
            first = count
            continue
        if fast == slow and count != 1 and flag == False:
            flag = False
            return count-first
    return None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        if get_cycle_num(head)!= None:
            n = get_cycle_num(head)
        else:
            return None
        for i in range(n):
            fast = fast.next
        while True:
            if fast == slow:
                return slow
            slow = slow.next
            fast = fast.next
'''
# 合并两个步骤，省去了把等差指针往后挪的过程
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        flag = True
        count = 0
        while fast:
            fast = fast.next.next if fast.next is not None else fast.next
            slow = slow.next
            count += 1
            if fast == slow and count != 1 and flag == True:
                flag = False
                continue
            if fast == slow and count != 1 and flag == False:
                break 
        if count == 1 or flag == True:
            return None             
        fast = head
        while True:
            if fast == slow:
                return slow
            slow = slow.next
            fast = fast.next

# @lc code=end

