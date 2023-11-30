# 可以用python的deepcopy直接完成
'''
# 在哈希表里使用原节点作为key，新节点作为value
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        Q = P = Node(0)
        N = M = head
        hashmap = {}
        if head == None:
            return None
        while head:
            hashmap[head] = Node(head.val)
            head = head.next
        head = M
        while M:
            if M.next:
                hashmap[M].next = hashmap[M.next]
            if M.random:
                hashmap[M].random = hashmap[M.random]
            M = M.next
        return hashmap[N]
'''
# 链表原地复制插入并断开
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        N = M = head
        if head == None:
            return None
        # 复制每一个节点
        while head:
            temp1 = head.next
            temp2 = head.random
            head.next = Node(head.val)
            head = head.next
            head.next = temp1
            head.random = temp2
            head = head.next
        # 把复制节点的random接到复制出来的节点上
        M = M.next
        while M:
            print(M.val)
            if M.random:
                M.random = M.random.next
            if M.next:
                M = M.next.next
            else:
                break
        res = start = N.next
        print("----------------")
        while start:
            print(start.val)
            if start.next:
                start.next = start.next.next
            else:
                break
            start = start.next
        return res