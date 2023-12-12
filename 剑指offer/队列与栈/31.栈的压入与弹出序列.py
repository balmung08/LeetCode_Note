'''
# 一个相对奇怪的思路：把问题分成三个情况来考虑
# 给putin和takeout都设置一个指针
# 如果目前要拿的书正好是书架上的最后一本，就取出这一本，关注下一本要取出的书
# 如果目前要放进去的书和要取出的书不一样，就把书放进书架，关注下一本要放进去的书
# 如果目前要取的书正好是要拿的书，直接不放进去了，开始关注下一本要取出的书
# 当书放完以后，书架上还有书，就一本一本取出来看是否是要取的书，实质是把书架list和剩下的takeout倒序对比是否相同
class Solution:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
        list_in = []
        position = 0
        i = 0
        while i<len(putIn):
            if list_in and list_in[-1] == takeOut[position]:
                list_in.pop()
                position += 1
            elif putIn[i] != takeOut[position]:
                list_in.append(putIn[i])
                i += 1
            else:
                i+=1
                position += 1
        return list_in == list(reversed(takeOut[position:]))
'''
# 常规思路，依次往里塞，如果相同就再拿出来，目标位后移
# 其实本质上思路差不多
class Solution:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
        list0 = []
        position = 0
        for i in putIn:
            list0.append(i) 
            while list0 and position<len(takeOut) and list0[-1] == takeOut[position]:
                list0.pop()
                position+=1
        return not list0