#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#

# @lc code=start
# 最基础的，直接考虑后面1-6格子的bfs由于要考虑的情况过多会超时
# 只考虑六格里的最后一个常规格和有传送的格子
# 注意棋盘是S型编号！铺平时进行特殊处理
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length0 = len(board)-1
        new_board = []
        board.reverse()
        for i in range(len(board)):
            if i % 2 == 0:
                for j in board[i]:
                    new_board.append(j)
            if i % 2 == 1:
                for j in reversed(board[i]):
                    new_board.append(j)
                
        length = len(new_board)-1
        visited = set()
        
        queue = [(0,0)] 
        while queue:
            point,cnt = queue.pop(0)
            max_nom = None
            for i in range(point+1,min(point+7,length+1)):
                if new_board[i] != -1:
                    if new_board[i]-1 not in visited:
                        queue.append((new_board[i]-1,cnt+1))
                        visited.add(new_board[i]-1)
                else:
                    if i not in visited:
                        visited.add(i)
                        max_nom = i
                if i == length or new_board[i]-1 == length:
                    # print(i,new_board[i]-1,length)
                    return cnt+1
            if max_nom:
                queue.append((max_nom,cnt+1))
        return -1
        
            
                    

# @lc code=end

