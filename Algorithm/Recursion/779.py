# K-th Symbol in Grammar
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        elif k > 2 ** (n - 2):
            return 1 - self.kthGrammar(n - 1, k - 2 ** (n - 2))
        else:
            return self.kthGrammar(n - 1, k)
