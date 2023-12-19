class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        abs = 1
        num = ""
        dict = {"1","2","3","4","5","6","7","8","9","0"}
        if str == "":
            return 0
        if str[0] == '+':
            pass
        elif str[0] == '-':
            abs = -1
        elif str[0] in dict:
            num = num+str[0]
        else:
            return 0
        for i in range(1,len(str)):
            if str[i] in dict:
                num = num+str[i]
            else:
                break
        if num == "":
            return 0
        # int可以改成迭代按位求总和
        num = int(num)
        if abs*num<-2147483648:
            return -2147483648
        elif abs*num>2147483647:
            return 2147483647
        else:
            return abs*num