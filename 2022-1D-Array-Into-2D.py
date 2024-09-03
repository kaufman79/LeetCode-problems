# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

class Solution(object):
    def construct2DArray(self, original, m, n):

        # check if possible
        if len(original) != m * n:
            return []

        # Initialize the result 2D array with m rows and n columns
        result_array = [[0] * n for _ in range(m)]

        index = 0
        for i in range(m):  # iterate through each row i
            for j in range(n):  # iterate through each column j
                result_array[i][j] = original[index]
                index += 1
        return result_array

# alternatively:
    def construct2DArray2(self, original, m, n):
        if m * n != len(original):
            return []

        # Initialize the result 2D array with m rows and n columns
        result_array = [[0] * n for _ in range(m)]

        # Fill the 2D array with elements from the original array
        for i in range(len(original)):
            # row, col = divmod(i, n)  # quotient, remainder of i / n...same as:
            row = i // n
            col = i % n
            result_array[row][col] = original[i]

        return result_array


original_array = [1,2,3,4,5,6]
m = 3
n = 2
solution = Solution()
print(solution.construct2DArray2(original_array, m=m, n=n))
