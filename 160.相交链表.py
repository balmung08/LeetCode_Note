#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
# 存下来直接遍历对比会超时
# 拿个字典存下来找，复杂度压到了n但是使用了额外的空间
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic = {}
        count = 0
        while headA:
            dic[headA] = count
            headA = headA.next
            count += 1
        while headB:
            if headB in dic:
                return headB
            headB = headB.next
        return None
'''
'''
# 如果使用集合来存就不需要记录位置，可以稍微加速
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic = set()
        while headA:
            dic.add(headA)
            headA = headA.next
        while headB:
            if headB in dic:
                return headB
            headB = headB.next
        return None
'''
'''
# 将列表入栈以后倒着吐出来，比较直到不相同为止，速度也挺慢

# 如果要只使用空间复杂度为1，时间复杂度又要n，可以使用下面方法
# 两链表遍历求长度，得到长度差值；多出来的这一段不可能有公共节点
# 把长链表先走这一段的长度，随后两个链表一起往后走进行比较
# 性能比上面略优一点，主要是占空间少了
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s1, s2 = 0, 0
        p, q = headA, headB
        # 计算长度
        while p:
            p = p.next
            s1 += 1
        while q:
            q = q.next
            s2 += 1
        p, q = headA, headB
        # 不确定谁比较长
        # for i in range负数时压根就不会执行，省去了判断语句
        for i in range(s1 - s2):
            p = p.next
        for i in range(s2 - s1):
            q = q.next
        while p and q and p != q:
            p = p.next
            q = q.next
        return p
'''
# 这个给我秀麻了，太牛逼了这是
# https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/210289/jiao-ni-yong-lang-man-de-fang-shi-zhao-dao-liang-2/
# 走你走过的路，是不是算程序里的浪漫了
# 另外，这个方法意外的比上面那个慢，不过这些n都在一个n数量级里，看运气的多
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p, q = headA, headB
        while not p == q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

# @lc code=end

