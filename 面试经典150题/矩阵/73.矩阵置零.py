#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
# mn:复制原数组，读复制数组来修改原本数组
# mn:也可以使用多维数组保存0出现的位置
# m+n:使用两个一维数组分别记录每行每列是否需要置零，读完以后再改
# 常量空间：使用两个变量记录第零行第零列是否需要置零，将是否需要置零信息保存到原数组这俩处，就不需要额外存储空间
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        M, N = len(matrix), len(matrix[0])
        # 记录首行首列情况
        row0, col0 = False, False
        for i in range(M):
            if matrix[i][0] == 0:
                col0 = True
        for j in range(N):
            if matrix[0][j] == 0:
                row0 = True
        # 其他需要置零的先把首行列置零了作为标签
        # 只要有零，这行列都得变0，所以上述操作不会影响结果
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 根据上述标签进行置零
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 根据标志位决定首行列是否需要置零
        if row0:
            for j in range(N):
                matrix[0][j] = 0
        if col0:
            for i in range(M):
                matrix[i][0] = 0

# @lc code=end

