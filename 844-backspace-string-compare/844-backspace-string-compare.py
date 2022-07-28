class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stack_state(s):
            stack = ""
            for c in s:
                if c == '#':
                    if len(stack)>0:
                        stack = stack[:-1]
                    continue
                stack += c
            return stack
        return stack_state(s)==stack_state(t)
        