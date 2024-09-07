# Reverse String


# Recursion
# T: O(n)
# S: O(n)
class Solution:
    def reverseString(self, s):
        def reverseStringRecur(s, left, right):
            if left >= right:
                return
            [s[left], s[right]] = [s[right], s[left]]
            reverseStringRecur(s, left + 1, right - 1)

        reverseStringRecur(s, 0, len(s) - 1)


# Recursion 수정
# T: O(n)
# S: O(n)
class Solution2:
    def reverseString(self, s):
        def reverseStringRecur(left, right):
            if left >= right:
                return
            [s[left], s[right]] = [s[right], s[left]]
            reverseStringRecur(left + 1, right - 1)

        reverseStringRecur(0, len(s) - 1)


# reverseStringRecur는 reverseString의 하위 메소드이기 때문에 굳이 s를 argument로
# 보낼 필요가 없음
