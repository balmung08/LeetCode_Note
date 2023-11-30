# 与LC21完全一样
class Solution:
    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        P = res = ListNode(0)
        while l1 and l2:
            if l1.val>=l2.val:
                res.next = l2
                l2 = l2.next
                res = res.next
            else:
                res.next = l1
                l1 = l1.next
                res = res.next
        if l1:
            res.next = l1
        elif l2:
            res.next = l2
        return P.next