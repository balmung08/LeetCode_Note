class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        if not array: return []
        l, r, t, b, res = 0, len(array[0]) - 1, 0, len(array) - 1, []
        while True:
            for i in range(l, r + 1): 
                res.append(array[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): 
                res.append(array[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): 
                res.append(array[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): 
                res.append(array[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res