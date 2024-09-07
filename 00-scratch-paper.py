class Solution:
    def method(self, original: list, rows, cols):
        if len(original) != rows * cols:
            return []

        res = [[0] * cols for row in range(rows)]
        index = 0

        for i in range(rows):
            for j in range(cols):
                res[i][j] = original[index]
                index += 1
        return res


sol = Solution()
print(sol.method(original=[1,2,3,4], rows=2, cols=2))