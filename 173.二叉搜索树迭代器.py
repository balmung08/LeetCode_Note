#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 解法1：递归中序遍历得到一个列表，随后根据列表内容进行处理
# 解法2：迭代遍历；初始化的时候获取最右节点作为结束判断
# 解法2的迭代过程完全处在next中，而stack在过程中会出现空的情况
# 因此不能使用stack为空进行结束判断 
'''
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.cur = root
        self.fin = True
        point = root
        while point.right:
            point = point.right
        self.fin_p = point
 
    def next(self) -> int:
        while self.stack or self.cur:
            while self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            self.cur = self.stack.pop()
            res = self.cur.val
            if self.cur == self.fin_p:
                self.fin = False
            self.cur = self.cur.right
            return res

    def hasNext(self) -> bool:
        return self.fin
'''
# 解法3：把迭代的前半部分，即塞进所有左子树的步骤放进初始化中
# 这样stack一旦为空则标志着遍历的结束
# 在方法2中执行完一次后会保持stack为空结束，在下一次再填充
# 方法3中获取完值以后直接填充，保证在next执行结束后不到结尾stack不为空
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.cur = root
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
    def next(self) -> int:
        self.cur = self.stack.pop()
        root = self.cur.right
        while root:   
            self.stack.append(root)
            root = root.left
        return self.cur.val
    def hasNext(self) -> bool:
        return not self.stack == []
# @lc code=end

