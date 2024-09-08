# Fibonacci Number


class Solution:
    def fib(self, n):
        if n < 2:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


# Memoization
class Solution2:
    def fib(self, n):
        cache = {}

        def fib_recur(n):
            if n in cache:
                return cache[n]

            if n < 2:
                return n

            result = fib_recur(n - 1) + fib_recur(n - 2)
            cache[n] = result
            return result

        return fib_recur(n)


# Memoization + Decorator Pattern
class Solution3:
    @staticmethod
    # 클래스 내부에서 정의되지만, 클래스 인스턴스와는 독립적으로 동작하는 매서드
    # 인스턴스나 클래스의 상태를 전혀 참조하지 않는 매서드를 정의할 때 사용
    # 클래스나 인스턴스와 관계없이 호출할 수 있는 메소드를 만들 때 유용
    # 즉, 클래스 내부에서 논리적으로 속하지만, 인스턴스 변수나 클래스 변수를
    # 사용할 필요가 없을 때 유용
    # self를 받지 않는다.
    def memoize(func):
        cache = {}

        def wrapper(*args):
            # *args는 가변 인자를 받을 때 사용하는 구문
            # 함수에 전달되는 모든 인자들을 튜플로 묶어서 처리
            if args in cache:
                return cache[args]
            result = func(*args)
            cache[args] = result
            return result

        return wrapper

    @memoize
    # 파이썬에서 Decorator 사용 문법
    def fib(self, n):
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
