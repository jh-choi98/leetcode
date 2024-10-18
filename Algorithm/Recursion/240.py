# Search a 2D Matrix 2


# Recursion
class Solution:
    def searchMatrix(self, mat, target):
        pass


# Iteration
class Solution2:
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
