from my_tokens import Integer, Float

class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def read_INT(self, value):
        return int(value)
    
    def read_FLT(self, value):
        return float(value)
    
    def compute(self, left, operator, right):
        left_type = left.type
        right_type = right.type
        
        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)


        if operator.value == '+':
            output = left + right
        elif operator.value == '-':
            output = left - right
        elif operator.value == '*':
            output = left * right
        elif operator.value == '/':
            output = left / right
        elif operator.value == '%':
            output = left % right
        
        #return the output in the ProLang's data types and not python's
        return Integer(output) if(left_type == 'INT' and right_type == 'INT') else Float(output)

    def interpret(self, tree = None):
        if tree == None:
            tree = self.tree

        left_node = tree[0]

        #if the left_node is a subtree, it will make recursive descent call to first resolve that
        if type(left_node) == list:
            left_node = self.interpret(left_node)
        
        right_node = tree[2]

        #if the left_node is a subtree, it will make recursive descent call to first resolve that
        if type(right_node) == list:
            right_node = self.interpret(right_node)
        
        #root node
        operator = tree[1]

        return self.compute(left_node, operator, right_node)