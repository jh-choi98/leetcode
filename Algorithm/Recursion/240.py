# Search a 2D Matrix 2
# Recursion - Decrease and Conquer
class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int):
        height = len(mat)
        width = len(mat[0])

        def search(start_row, start_col):
            if start_row >= height or start_col < 0:
                return False
            if mat[start_row][start_col] == target:
                return True

            if mat[start_row][start_col] > target:
                return search(start_row, start_col - 1)
            else:
                return search(start_row + 1, start_col)

        return search(0, width - 1)


# Recursion - Divide and Conquer
class Solution2:
    def searchMatrix(self, mat: List[List[int]], target: int):
        # [] 나 [[]]가 주어졌을 때
        if not mat or not mat[0]:
            return False

        def search(left, top, right, bottom):
            if left > right or top > bottom:
                return False
            # target이 서브 행렬에 존재할 수 없는 경우
            if target < mat[top][left] or target > mat[bottom][right]:
                return False

            mid_col = (left + right) // 2
            row = top
            # 중간 열에서 target이 들어갈 수 있는 행을 찾음
            while row <= bottom and mat[row][mid_col] <= target:
                if mat[row][mid_col] == target:
                    return True
                row += 1
            return (row <= bottom and search(left, row, mid_col - 1, bottom)) or (
                row - 1 >= top and search(mid_col + 1, top, right, row - 1)
            )

        return search(0, 0, len(mat[0]) - 1, len(mat) - 1)


# Iteration
class Solution3:
    def searchMatrix(self, mat, target):
        height = len(mat)
        width = len(mat[0])
        i, j = 0, width - 1
        while i < height and j >= 0:
            if target == mat[i][j]:
                return True
            if mat[i][j] > target:
                j -= 1
            else:
                i += 1

        return False
