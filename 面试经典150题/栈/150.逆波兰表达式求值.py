#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if i == "+":
                stack.append(stack.pop()+stack.pop())
            elif i == "-":
                stack.append(-stack.pop()+stack.pop())
            elif i == "*":
                stack.append(stack.pop()*stack.pop())
            elif i == "/":
                stack.append(int(1/stack.pop()*stack.pop()))
            else:
                stack.append(int(i))
        return stack[0]

# @lc code=end

