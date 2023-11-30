# 可以塞进链表反转、塞进栈再输出、递归往后推移，时间复杂度空间复杂度均相同
class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.reverse()
        return res