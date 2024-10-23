# Happy Number
class Solution:
    def isHappy(self, n: int):
        hashset = set()
        sum_digits = n
        digit_list = []

        while True:
            if sum_digits == 1:
                return True
            elif sum_digits in hashset:
                return False
            else:
                hashset.add(sum_digits)

            while sum_digits > 0:
                digit_list.append(sum_digits % 10)
                sum_digits = sum_digits // 10

            digit_list = list(map(lambda x: x**2, digit_list))
            sum_digits = sum(digit_list)
            digit_list = []


# Happy Number
class Solution2:
    def isHappy(self, n: int):
        hashset = set()
        sum_digits = n
        digit_list = []

        while sum_digits != 1 and sum_digits not in hashset:
            hashset.add(sum_digits)

            while sum_digits > 0:
                digit_list.append(sum_digits % 10)
                sum_digits = sum_digits // 10

            digit_list = list(map(lambda x: x**2, digit_list))
            sum_digits = sum(digit_list)
            digit_list = []

        return sum_digits == 1


class Solution3:
    def isHappy(self, n: int):
        seen = set()

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)  # 몫과 나머지를 한 번에 반환
                total_sum += digit**2
            return total_sum

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
