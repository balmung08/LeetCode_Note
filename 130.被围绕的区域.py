#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
# 不能从一般位置开始
# 从边界开始，边界相连的全部标记出来，他们不会变成x
# 其他的o全部变成x
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(i,j):
            if board[i][j] == "O":
                board[i][j] = "-"
                List = [[i,j]]
                while List:
                    x,y = List.pop(0)
                    for new_x, new_y in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                        if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == 'O':
                            board[new_x][new_y] = '-' 
                            List.append([new_x, new_y])
        for i in range(len(board)):
            bfs(i,0)
            bfs(i,len(board[0])-1)
        for i in range(len(board[0])):
            bfs(0,i)
            bfs(len(board)-1,i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "-":
                    board[i][j] = "O"



# @lc code=end

