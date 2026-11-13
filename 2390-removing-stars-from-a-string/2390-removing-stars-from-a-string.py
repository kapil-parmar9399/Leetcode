class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in s :
            if len(stack) ==0 and i != '*':
                stack.append(i)

            elif i == '*':
                stack.pop()

            else:
                stack.append(i)


        return "".join(stack)               