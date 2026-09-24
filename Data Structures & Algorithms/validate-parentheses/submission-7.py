class Solution:
    def isValid(self, s: str) -> bool:
        m={"}":"{", "]":"[",")":"("}
        stack=[]
        for c in s:
            if c in m:
                if stack and m[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

