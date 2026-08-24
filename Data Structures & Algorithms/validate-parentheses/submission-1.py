class Solution:
    def isValid(self, s: str) -> bool:
            stack=[]
            matchingB={')' : '(', ']' : '[' ,'}' : '{'}
            for character in s:
                if character in matchingB:
                    if stack and stack[-1] == matchingB[character]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(character)
            return not stack                    