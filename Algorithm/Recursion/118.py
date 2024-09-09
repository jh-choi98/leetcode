# Pascal's Triangle


# Recursion
class Solution:
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]

        triangle = self.generate(numRows - 1)

        prev_row = triangle[-1]
        cur_row = [1]

        for i in range(1, len(prev_row)):
            cur_row.append(prev_row[i - 1] + prev_row[i])
        cur_row.append(1)

        triangle.append(cur_row)
        return triangle
