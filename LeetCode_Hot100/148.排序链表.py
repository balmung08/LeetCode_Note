#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# 先试试朴素的遍历出来，排序后新建列表
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        P = head
        num = []
        while head:
            num.append(head.val)
            head = head.next
        num.sort()
        Q = res = ListNode()
        for i in num:
            res.next = ListNode(i)
            res = res.next
        return Q.next
# 时间复杂度是n+nlogn，基本上是最快的，但是空间复杂度很高
'''
'''
# 自顶向底的标准归并排序，空间复杂度是logn(递归了logn次开辟的空间)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 头节点为空或只有头节点直接返回
        if not head or not head.next: return head 
        # 快慢双指针找到链表中点
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        # mid找到终点位置
        mid, slow.next = slow.next, None 
        # 头和中间为开始的左右两半进行递归
        left, right = self.sortList(head), self.sortList(mid)
        # 开始合并与排序
        h = res = ListNode(0)
        while left and right:
            # 如果右半比左半大，左半的拼进h里
            if left.val < right.val: 
                h.next, left = left, left.next
            # 反之
            else: 
                h.next, right = right, right.next
            h = h.next
        # 左右可能会长度差一个，把差的那个填进去
        h.next = left if left else right
        return res.next
'''
# 自下向上的归并排序，使用迭代，速度最慢
# 直接一步到位拆到最散，随后直接迭代开始合并，不需要使用递归
# 这种归并排序适合链表，不需要创建新节点，改变顺序即可
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        # 获取链表长度
        while h: h, length = h.next, length + 1
        # 哨兵节点
        res = ListNode(0,head)

        # 1，2，4，8 intv表示分段的长度
        while intv < length:
            pre, h = res, res.next
            # 直到h到达链表最后，否则持续合并
            while h:
                # 按照intv进行片段切分，一次切两个
                h1, i = h, intv
                while i and h: 
                    h, i = h.next, i - 1
                # 如果h1到达链表最后，则不需要进行下一段切分比较了
                # 已经没有h2了，不需要后续步骤
                if i: 
                    break 
                h2, i = h, intv
                while i and h: 
                    h, i = h.next, i - 1
                # 获取了要比较的两个分段的长度，h1，h2是头节点
                c1, c2 = intv, intv - i 
                # 左右链表比较与合并
                while c1 and c2:
                    if h1.val < h2.val: 
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: 
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2

                # 上面把剩余的接到了后面，但是pre这一头节点还在原本位置
                # 按照剩余那个链表的长度把pre往后挪到正确的位置
                while c1 > 0 or c2 > 0: 
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                # 修正pre后面为待切分的剩余链表
                pre.next = h 
            intv *= 2
        return res.next


# @lc code=end

