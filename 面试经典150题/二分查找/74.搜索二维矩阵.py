#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
# 横找一次竖找一次
# 也可以把矩阵展开为一维以后直接一次二分完事
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first = 0 
        last = len(matrix)-1
        while last >= first:
            if matrix[(last+first)//2][0]>target:
                last = (last+first)//2-1
            elif matrix[(last+first)//2][0]<target:
                first = (last+first)//2+1
            elif matrix[(last+first)//2][0]==target:
                return True
        h = first-1
        if h<0:
            return False
        first = 0
        last = len(matrix[0])-1
        while last >= first:
            if matrix[h][(last+first)//2]>target:
                last = (last+first)//2-1
            elif matrix[h][(last+first)//2]<target:
                first = (last+first)//2+1
            elif matrix[h][(last+first)//2]==target:
                return True
        return False
# @lc code=end

