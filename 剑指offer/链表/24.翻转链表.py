# 与LC206完全一样
class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        while head:
            tmp = head.next
            head.next = res
            res = head
            head = tmp
        return res