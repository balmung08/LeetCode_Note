#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
# 使用列表来完成不常用数据的删除很显然不是常数复杂度
# get/put要是常数就说明扫描数据和删除数据都必须是常数复杂度
# get/put要求常数时间复杂度只能使用哈希表，存储序号和节点指针
# 要完成不使用额外的内容来记录被访问的信息
# 可以使用链表，访问以后就把节点拉到最前面去，超出内存的删除
# 要删除节点需要前一个节点的指针，但是哈希表只能返回本节点
# 故使用双向链表+哈希表的结构
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        # 新建哈希表与链表的头尾节点
        self.capacity = capacity
        self.hashm = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    # 写一个专门用于把指定节点放到头节点的函数
    def tohead(self,key):
        target = self.hashm[key]
        # 把这个节点的上下节点接起来
        target.prev.next = target.next
        target.next.prev = target.prev
        # 把target移到头节点后面(先改target再改前后)
        target.prev = self.head
        target.next = self.head.next
        self.head.next.prev = target
        self.head.next = target
    def get(self, key: int) -> int:
        # 访问已有节点就把节点拉到头部
        if key in self.hashm:
            self.tohead(key)
        # get后面那个值是找不到的时候返回的默认值
        res = self.hashm.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value
    def put(self, key: int, value: int) -> None:
        # 节点存在就更新节点内存并拉到头部
        if key in self.hashm:
            self.hashm[key].value = value
            self.tohead(key)
        else:
            # 节点如果满了就去掉尾节点前的节点并去掉哈希表项
            if len(self.hashm) == self.capacity:
                self.hashm.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
            # 如果不在的话就插入到头节点后
            new = ListNode(key, value)
            self.hashm[key] = new   
            new.prev = self.head
            new.next = self.head.next
            self.head.next.prev = new
            self.head.next = new







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

