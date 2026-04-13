class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapped = {"(" : ")", "[" : "]", "{" : "}"}

        for c in s:
            if c in mapped:
                stack.append(c)

            elif(c in mapped.values()):
                if stack and c == mapped[stack[-1]]:
                    stack.pop()

            else:
                return false
        
        return len(stack) == 0 

                

