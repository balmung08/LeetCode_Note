# 和LC19思路一模一样
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        Q = P = S = ListNode(0,head)
        for i in range(0,cnt):
            S = S.next
        while S.next:
            P = P.next
            S = S.next
        return P.next