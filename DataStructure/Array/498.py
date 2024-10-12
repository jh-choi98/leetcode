# Diagonal Traverse

from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, mat):
        new_arr = []
        is_upward = True
        out_loop_len = len(mat)
        in_loop_len = len(mat[0])
        i = 0
        j = 0

        while i < out_loop_len and j < in_loop_len:
            new_arr.append(mat[i][j])
            if is_upward:
                if j == in_loop_len - 1:
                    i = i + 1
                    is_upward = not is_upward
                elif i == 0:
                    j = j + 1
                    is_upward = not is_upward
                else:
                    i = i - 1
                    j = j + 1
            else:
                if i == out_loop_len - 1:
                    j = j + 1
                    is_upward = not is_upward
                elif j == 0:
                    i = i + 1
                    is_upward = not is_upward
                else:
                    i = i + 1
                    j = j - 1
        return new_arr


class Solution2:
    def findDiagonalOrder(self, mat):
        d = defaultdict(list)
        out_loop_len = len(mat)
        in_loop_len = len(mat[0])

        for i in range(out_loop_len):
            for j in range(in_loop_len):
                d[i + j].append(mat[i][j])

        ans = []
        for entry in d.items():
            if entry[0] % 2 == 0:
                ans.extend(entry[1][::-1])
            else:
                ans.extend(entry[1])
        return ans
