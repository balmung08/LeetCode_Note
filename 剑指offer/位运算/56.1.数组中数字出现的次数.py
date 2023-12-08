# 空间复杂度为常数就不能使用哈希表
# 位运算具有交换律且n个相同的数取异或都为0
# 如果可以把数组分为两组，每组都由一个单独的和一些成对的数组成
# 根据任意一位进行区分，两个相同的数都应该在同一组里
class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        x,y,tmp = 0,0,0
        m = 1
        for i in range(0,len(sockets)):
            tmp = sockets[i]^tmp
        # m获取tmp最低位的1
        while tmp & m == 0: # m 循环左移一位，直到 z & m ！= 0
            m <<= 1
        for num in sockets:
            if num & m == m:
                x = x^num
            elif num & m == 0:
                y = y^num
        return[x,y]
