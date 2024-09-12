# Pascal's Triangle 2
class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        prev_row = self.getRow(rowIndex - 1)
        cur_row = [1]

        for i in range(1, len(prev_row)):
            cur_row.append(prev_row[i - 1] + prev_row[i])
        cur_row.append(1)
        return cur_row
