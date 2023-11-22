
class Solution:
    def decodeString(self, s: str):
        stack = []
        #res = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                tmpStr = ''
                while stack and stack[-1] != '[':
                        tmpStr = stack.pop() + tmpStr
                if stack:
                    stack.pop()
                    num = ''

                    while stack and stack[-1].isdigit():
                        num = stack.pop() + num
                    tmpStr = tmpStr * int(num)
                    while stack and stack[-1] != '[':
                        tmpStr = stack.pop() + tmpStr
                stack.append(tmpStr)                
        return ''.join(stack)

    def decodeStringFirstVersionTooCompels(self, s: str) -> str:
        stack = []
        res = []
        terms = s.split(']')
        for t in reversed(terms):
            pattern = t.split('[')
            while pattern:
                if len(pattern) == 1:
                    stack.append(pattern[0])
                    pattern.pop()
                else:
                    pattern,outp,inp = pattern[:-2],pattern[-2],pattern[-1]
                    stack.append(''.join([inp for _ in range(int((outp)))]))
            res = stack + res
        return ''.join(res)