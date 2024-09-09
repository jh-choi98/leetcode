# Pascal's Triangle


# DP
# 각 행의 값은 이전 행의 값들을 이용해 계산되는데, 이전에 계산된 결과(삼각형의 각 행)를
# 메모리에 저장해 두고, 이를 사용하여 새로운 행을 계산한다.
# DP은 문제를 작은 하위 문제들로 나누고, 그 결과를 저장하여 같은 계산을 반복하지 않도록
# 하는 기법이다.
class Solution:
    def generate(self, numRows):
        triangle = []

        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            # 길이가 row_num + 1인 리스트를 생성하며, 그 리스트의 모든 요소는 None으로 초기화된다.
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle


# Recursion
class Solution:
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]

        # 재귀적으로 이전 파스칼 삼각형 생성
        triangle = self.generate(numRows - 1)

        # 현재 행을 이전 행을 기반으로 계산
        prev_row = triangle[-1]
        current_row = [1]

        for i in range(1, len(prev_row)):
            current_row.append(prev_row[i - 1] + prev_row[i])

        current_row.append(1)
        triangle.append(current_row)

        return triangle
