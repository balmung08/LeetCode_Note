#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 可以理解成把后面的第k个列表拆下来，并把最后节点接到头节点上
# 异常处理空链表、k可以被列表长度整除等需要返回原链表的特殊情况
# 这种时候第二次遍历直接遍历完了，拿不到新的头节点，就返回原本的头节点
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        P = head
        Q = head
        length = 0
        if head == None:
            return head
        while head.next:
            head = head.next
            length+=1
        length+=1
        if k%length==0:
            return P
        # 此时head是原本的尾节点
        for i in range(length - k%length-1):
            Q = Q.next
        M = Q.next 
        Q.next = None
        head.next = P
        return M


# @lc code=end

