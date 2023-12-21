'''
# 奇偶分离合并返回
# 空间复杂度很大
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        G,O= [],[]
        for i in actions:
            if i%2:
                G.append(i)
            else:
                O.append(i)
        return G+O
'''
'''
# 原地解决
# 反向双指针交换
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        start = 0
        end = len(actions)-1
        while end>start:
            if actions[start]%2:
                start += 1
            else:
                actions[start],actions[end] = actions[end],actions[start]
                end-=1
        return actions
'''
# 同向双指针交换
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        slow, fast = 0, 0
        ln = len(actions)
        while fast in range(ln):
            if actions[fast] % 2:
                actions[slow], actions[fast] = actions[fast], actions[slow]
                slow += 1
            fast += 1
        return actions