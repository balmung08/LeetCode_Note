class Solution:
    def pathEncryption(self, path: str) -> str:
        res = ""
        for i in range(len(path)):
            if path[i] == '.':
                res += ' '
            else:
                res += path[i]
        return res