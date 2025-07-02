class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            '(': ')',
            '{': '}',
            '[': ']'   
        }

        st = []
        for c in s:
            if c not in hm:
                if st and c == hm[st[-1]]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)

        return not st

class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")": "(", "]": "[", "}": "{"}
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return not stack
