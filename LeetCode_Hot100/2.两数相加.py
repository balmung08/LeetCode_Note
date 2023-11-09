#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list. 
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

'''
# 转成数字再相加生成链表，得亏这是python int类型长度没上限的,不然大样本要爆        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = P = ListNode()
        count = 0
        sum1 = 0
        sum2 = 0
        l = l1
        n = []
        while True:
            a = l.val
            sum1 += a * (10**count)
            count += 1
            if l.next == None:
                break
            l = l.next
        l = l2
        count = 0
        while True:
            a = l.val
            sum2 += a * (10**count)
            count += 1
            if l.next == None:
                break
            l = l.next
        sum = sum1 + sum2
        for i in range(len(str(sum))-1,-1,-1):
            x = sum // (10**i)
            #print(sum // (10**i),sum)
            sum -= (10**i) * (sum // (10**i))
            n.append(x)
        n.reverse()
        for i in n:
            print(i)
            P.next = ListNode(i)
            P = P.next
        return d.next
'''
'''
# 逐位相加，最后时间居然和转成数字再相加差不多，本来复杂度也一样
#  divmod(a,b)  return(a // b, a % b)。
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = P = ListNode()
        flag = False
        end1 = end2 = False
        while True:
            if end1 == False:
                a = l1.val
            else: 
                a = 0
            if end2 == False:
                b = l2.val
            else: 
                b = 0
            s = a + b
            if flag == True:
                s += 1
                flag = False
            if s >= 10:
                s -= 10
                flag = True
            print(s)
            P.next = ListNode(s)
            P = P.next
            if l1.next != None:
                l1 = l1.next
            else:
                end1 = True
            if l2.next != None:
                l2 = l2.next
            else: 
                end2 = True
            if end1 == True and end2 == True and flag == False:
                break
        return d.next
'''

# 最快的解法，思路差不多但是没有设置标志位，减少了标志位赋值的时间
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        result = ListNode(0)
        root = result
        carry = 0
        while p1 or p2 or carry:
            v1 = (p1.val if p1 else 0)
            v2 = (p2.val if p2 else 0)

            res = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            result.next = ListNode(res)

            p1 = (p1.next if p1 else None)
            p2 = (p2.next if p2 else None)
            result = result.next
        return root.next

# @lc code=end

