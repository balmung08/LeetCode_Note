#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start

# 采用树的结构，同样的前缀存在一个子树上
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

