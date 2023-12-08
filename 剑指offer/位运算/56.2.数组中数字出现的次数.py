# 没有空间要求，可以用哈希表
class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0  # 记录当前 bit 有多少个1
            bit = 1 << i  # 记录当前要操作的 bit
            # 当前位全部取异或
            for num in actions:
                if num & bit != 0:
                    cnt += 1
            # 每个位数可能出现1的次数是3的倍数和3的倍数+1次
            # 3次出现1说明目标数这一位是0
            if cnt % 3 != 0:
                res |= bit
        # python负数的存储方式有问题，需要特殊处理
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res