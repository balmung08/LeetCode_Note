#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
# 队列塞进去以后bank里就要去除，防止重复
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        possible_dict = {
                        "A": "CGT",
                        "C": "AGT",
                        "G": "ACT",
                        "T": "ACG"}
        queue = [(startGene,0)]
        while queue:
            Gene,cnt = queue.pop(0)
            if Gene == endGene:
                return cnt
            for index,content in enumerate(Gene):
                for p in possible_dict[content]:
                    temp = Gene[:index]+p+Gene[index+1:]
                    if temp in bank:
                        bank.remove(temp)
                        queue.append((temp,cnt+1))
        return -1


# @lc code=end

