#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# 粗暴遍历找到正数的节点位置，回推，走了两次循环
# 最后一次next找不到的时候说明已经到底了，异常处理之间跳过，下次循环就跳出了
# n以后不需要额外赋值走完了，之间把剩下的接上就完事
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        P = S = ListNode(0,head)
        Q = head
        count = c = 0
        while Q:
            Q = Q.next
            count += 1
        for i in range(1,count-n+1):
            S = S.next
        S.next = S.next.next
        return P.next
'''
# 一趟循环完事就得使用双指针了
# 这个方法不用像找长度一样遍历一遍所有节点，理论上快一些
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Q = P = S = ListNode(0,head)
        for i in range(0,n):
            S = S.next
        while S.next:
            P = P.next
            S = S.next
        P.next = P.next.next
        return Q.next

# @lc code=end

