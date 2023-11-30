class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        P = Q = ListNode(0)
        P.next = head
        while Q:
            if Q.next.val == val:
                Q.next = Q.next.next
                break
            Q = Q.next
        return P.next