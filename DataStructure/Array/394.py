class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
                
        return ''.join(stack)

class Solution2:
    def decodeString(self, s: str) -> str:
        def helper(i: int) -> tuple[str, int]:
            decoded = ""
            k = 0
            
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    sub_str, i = helper(i + 1)
                    decoded += num * sub_str
                elif s[i] == ']':
                    return decoded, i
                i += 1
                
            return decoded, i
        
        result, _ = helper(0)
        return result
            