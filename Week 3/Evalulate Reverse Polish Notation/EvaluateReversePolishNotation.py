class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token = tokens.pop()
        if token == '+' or token == '-' or token == '*' or token == '/':
            return self.eval(token, self.evalRPN(tokens), self.evalRPN(tokens))
        else:
            return int(token)
    
    def eval(self, operator, op2, op1):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            return int(op1 / op2)