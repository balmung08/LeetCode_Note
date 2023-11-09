#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# 这玩意居然能有98个点的性能？？？真就看运气刷点呗
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        P = L = ListNode()
        while True:
            if list1 != None and list2 != None and list1.val>=list2.val:
                L.next = ListNode(list2.val)
                L = L.next
                list2 = list2.next
            elif list1 != None and list2 != None and list1.val<list2.val:
                L.next = ListNode(list1.val)
                L = L.next
                list1 = list1.next
            elif list1 == None and list2 != None:
                L.next = ListNode(list2.val)
                L = L.next
                list2 = list2.next
            elif list1 != None and list2 == None:
                L.next = ListNode(list1.val)
                L = L.next
                list1 = list1.next
            elif list1 == None and list2 == None:
                break
        return P.next
'''
# 好看了点，但是本质上速度没啥变化
# 这题速度都大差不差，没必要硬刷了
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        P = L = ListNode()
        # 不处理所有节点里的最后一个节点
        while list1 and list2:
            if list1.val>=list2.val:
                L.next = ListNode(list2.val)
                list2 = list2.next
                L = L.next
            elif list1.val<list2.val:
                L.next = ListNode(list1.val)
                list1 = list1.next
                L = L.next
        # 这俩链表就剩一个了，哪个不为空之间接上
        L.next = list1 if list1 else list2
        return P.next
# @lc code=end

