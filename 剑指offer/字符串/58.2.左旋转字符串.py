# python切片
# 如果不能用切片，就分两部分塞进新列表即可
class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        return password[target:]+password[:target]
