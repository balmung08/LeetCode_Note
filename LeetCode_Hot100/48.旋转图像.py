#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start

# 可以很容易的知道两个元素之间的关系有
# matrix[i][j]->matrix[j][L-1-i]
# 如果直接使用这个关系进行遍历，则需要额外的存储空间
'''
# 矩阵两次反转，先转置再镜像，可以原地完成
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L = len(matrix)
        # 转置
        for i in range(0,L):
            for j in range(i,L):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # 镜像
        for i in range(0,L):
            for j in range(0,L//2):
                matrix[i][j],matrix[i][L-1-j] = matrix[i][L-1-j],matrix[i][j]
'''
# 四个元素一起找规律
# 分成四个象限进行变化
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

# @lc code=end

