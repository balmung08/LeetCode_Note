# 与LC160完全相同
'''
# 先找插值，往后找相同节点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A = 0
        len_B = 0
        tempA = headA
        tempB = headB
        while tempA:
            tempA = tempA.next
            len_A += 1
        while tempB:
            tempB = tempB.next
            len_B += 1
        if len_A>=len_B:
            for i in range(len_A-len_B):
                headA = headA.next
        else:
            for i in range(len_B-len_A):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
'''
# 链表浪漫解法：
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        P = headA
        Q = headB
        # 如果没有交点，两边交叉走完以后都为None，也会跳出循环
        while headA != headB:
            if headA:
                headA = headA.next
            else:
                headA = Q
            if headB:
                headB = headB.next
            else:
                headB = P
        return headA