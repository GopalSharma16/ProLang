class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

    def parse(self):
        return self.expression()

    def factor(self):
        if self.token.type == 'INT' or self.token.type == 'FLT':
            return self.token

    def term(self):
        left_node = self.factor()
        self.move()
        # it can only handle single operation i.e. only two operands and one operator
        while self.token.value == '%' or self.token.value == '*' or self.token.value == '/':
            operator = self.token
            self.move()
            right_node = self.factor()
            self.move()
            left_node = [left_node, operator, right_node]
        return left_node

    def expression(self):
        left_node = self.term()
        while self.token.value == '+' or self.token.value == '-':
            operator = self.token
            self.move()
            right_node = self.term()
            left_node = [left_node, operator, right_node]
        return left_node

    def move(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]