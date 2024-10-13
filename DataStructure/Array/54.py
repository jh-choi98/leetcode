class Solution:
    def spiralOrder(self, mat):
        new_arr = []

        top_offset = 0
        bottom_offset = 0
        left_offset = 0
        right_offset = 0

        width = len(mat[0])
        height = len(mat)
        total_len = width * height

        direction = 0
        i = 0
        j = 0

        while len(new_arr) < total_len:
            if direction == 0:
                if j == width - right_offset - 1:
                    direction += 1
                    top_offset += 1
                else:
                    new_arr.append(mat[i][j])
                    j += 1
            elif direction == 1:
                if i == height - bottom_offset - 1:
                    direction += 1
                    right_offset += 1
                else:
                    new_arr.append(mat[i][j])
                    i += 1
            elif direction == 2:
                if j == left_offset:
                    direction += 1
                    bottom_offset += 1
                else:
                    new_arr.append(mat[i][j])
                    j -= 1
            elif direction == 3:
                if i == top_offset:
                    direction = 0
                    left_offset += 1
                else:
                    new_arr.append(mat[i][j])
                    i -= 1

        return new_arr
