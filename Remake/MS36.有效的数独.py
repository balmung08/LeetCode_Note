#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
'''
# 可以九行九列九个区域分别检测，但是太暴力了没啥意义
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):                        #对每一行进行判断
            storage = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in storage:
                    return False
                else:
                    storage.append(board[i][j])
        for i in range(9):                         #对每一列进行判断
            storage = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in storage:
                    return False
                else:
                    storage.append(board[j][i])
        for i in range(0, 9, 3):                   #对九宫格是否重复进行判断
            for j in range(0, 9, 3):
                storage = []
                for x in range(0, 3):
                    for y in range(0, 3):
                        if board[i + x][j + y] == '.':
                            continue
                        if board[i + x][j + y] in storage:
                            return False
                        else:
                            storage.append(board[i + x][j + y])
        return True
'''
# 使用哈希表
# 记录行和数字出现次数
# 二维列表的行是行、列、块，列是按照坐标一次1-9的出现次数
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]
        # 如果每一行、列、块中有出现过就直接返回false
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    # b是核心步骤，判断其出现在哪个块里
                    b = (i // 3) * 3 + j // 3
                    if row[i][num] or col[j][num] or block[b][num]:
                        return False
                    row[i][num] = col[j][num] = block[b][num] = 1
        return True
# @lc code=end

