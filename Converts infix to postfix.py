class InfixToPostfixConverter:
    def __init__(self):
        self.infix = ""
        self.postfix = ""
        self.stack = []

    def get_infix(self, expression):
        self.infix = expression

    def show_infix(self):
        print("Infix Expression:", self.infix)

    def show_postfix(self):
        print("Postfix Expression:", self.postfix)

    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        return 0

    def convert_to_postfix(self):
        self.postfix = ""
        self.stack = []

        for symbol in self.infix:
            if symbol.isalnum():
                self.postfix += symbol
            elif symbol == '(':
                self.stack.append(symbol)
            elif symbol == ')':
                while self.stack and self.stack[-1] != '(':
                    self.postfix += self.stack.pop()
                self.stack.pop()  # Discard the '('
            elif symbol in {'+', '-', '*', '/'}:
                while (self.stack and self.precedence(self.stack[-1]) >= self.precedence(symbol)):
                    self.postfix += self.stack.pop()
                self.stack.append(symbol)

        while self.stack:
            self.postfix += self.stack.pop()

# Test expressions
expressions = [
    "A + B - C;",
    "(A + B) * C;",
    "(A + B) * (C - D);",
    "A + ((B + C) * (E - F) - G) / (H - I);",
    "A + B * (C + D) - E / F * G + H;"
]

for expression in expressions:
    converter = InfixToPostfixConverter()
    converter.get_infix(expression[:-1])
    converter.convert_to_postfix()
    converter.show_infix()
    converter.show_postfix()
    print()
