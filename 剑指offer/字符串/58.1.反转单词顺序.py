'''
# python api，去空格分割组合
# 不过这就没啥意义了
class Solution:
    def reverseMessage(self, message: str) -> str:
        return ' '.join(message.strip().split()[::-1])
'''
'''
# 遍历条件判断分割再翻转组合
class Solution:
    def reverseMessage(self, message: str) -> str:
        start = 0
        end = 0 
        tmp = ""
        res = []
        r = ""
        while start<len(message):
            if message[start] == " " and message[end] == " ":
                start+=1
                end = start
            elif message[start] == " ": 
                res.append(tmp)
                tmp = ""
                start += 1
                end = start
            elif start == len(message)-1:
                tmp+=message[start]
                res.append(tmp)
                start += 1
            else:
                tmp+=message[start]
                start += 1
        res.reverse()
        for i in range(len(res)):
            if i == len(res)-1:
                r+=(res[i])
            else:
                r+=(res[i]+" ")
        return r
'''

# 直接倒序遍历分割再符合，少一次翻转
# 思路和上面一模一样，不过可以使用strip把空格去掉，不用再以开始一起走了
class Solution:
    def reverseMessage(self, message: str) -> str:
        message = message.strip()                      # 删除首尾空格
        i = j = len(message) - 1
        res = []
        while i >= 0:
            while i >= 0 and message[i] != ' ': 
                i -= 1 # 搜索首个空格
            res.append(message[i + 1: j + 1])          # 添加单词
            while i >= 0 and message[i] == ' ': 
                i -= 1 # 跳过单词间空格
            j = i                                      # j 指向下个单词的尾字符
        return ' '.join(res)                           # 拼接并返回

