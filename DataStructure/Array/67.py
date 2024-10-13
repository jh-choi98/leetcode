class Solution:
    def addBinary(self, a: str, b: str):
        max_len = max(len(a), len(b)) + 1
        new_a = a.zfill(max_len)
        new_b = b.zfill(max_len)
        new_str = ""

        carry = 0
        for i in range(max_len - 1, -1, -1):
            if i == 0 and carry == 0:
                break
            sum_digit = int(new_a[i]) + int(new_b[i]) + carry
            if sum_digit >= 2:
                sum_digit -= 2
                carry = 1
            else:
                carry = 0
            new_str = str(sum_digit) + new_str

        return new_str


class Solution:
    def addBinary2(self, a: str, b: str):
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
