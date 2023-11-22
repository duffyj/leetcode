class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = [p for p in path.split('/') if p]
        for p in path:
            if p == '.':
                continue
            elif p == '..':
                if  stack:
                    stack.pop()
            else:
                stack.append(p)
        res = '/'.join(stack)
        return f'/{res}'
        