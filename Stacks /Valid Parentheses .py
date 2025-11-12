class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        closeToOpen = {')': '(', '}': '{', ']': '['}

        for c in s:
            # If it's a closing bracket
            if c in closeToOpen:
                # Pop the top element if stack is not empty, else assign dummy value
                top = stack.pop() if stack else '#'
                # Check if it matches the corresponding opening bracket
                if top != closeToOpen[c]:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(c)

        # If the stack is empty, all brackets were properly closed
        return not stack
