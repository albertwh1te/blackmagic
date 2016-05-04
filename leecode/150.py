# coding=utf-8
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in range(0, len(tokens)):
            operators = ["*", "+", "-", "/"]
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "*":
                    c = b * a
                if tokens[i] == "+":
                    c = b + a
                if tokens[i] == "-":
                    c = b - a
                if tokens[i] == "/":
                    if b / a < 0 and b % a != 0:
                        c = b / a + 1
                    else:
                        c = b / a
                stack.append(c)
        i += 1
        return stack[0]
