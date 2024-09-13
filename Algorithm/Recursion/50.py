# Pow(x, n)


"""
Binary exponentitation, a.k.a exponentiation by squaring, is a technique
for efficiently computing the power of a number. By repeatedly squaring x
and halving n, we can quickly compute x^n using a logarithmic number of
multiplication
"""


# Binary Exponentiation + Recursion
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -1 * n)

        if n % 2 == 1:
            return x * self.myPow(x * x, (n - 1) / 2)
        else:
            return self.myPow(x * x, n / 2)


# Binary Exponentiation + Tail recursion
class Solution2:
    def myPow(self, x, n):
        def myPowRecur(x, n, acc):
            if n == 0:
                return acc
            if n % 2 == 1:
                return myPowRecur(x * x, (n - 1) / 2, x * acc)
            else:
                return myPowRecur(x * x, n / 2, acc)

        if n < 0:
            return myPowRecur(1 / x, -1 * n, 1)
        else:
            return myPowRecur(x, n, 1)
