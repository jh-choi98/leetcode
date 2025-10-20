import math

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        s += '+'
        
        for i, ch in enumerate(s):
            if ch == ' ':
                continue
            
            if ch.isdigit():
                num = num * 10 + int(ch)
                
            if (ch in '+-*/') or (i == len(s) - 1):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    stack.append(math.trunc(prev / num))
                sign = ch
                num = 0
                
        return sum(stack)
