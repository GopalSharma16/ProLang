#Defines the type and value of the tokens
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    #to return the value instead of the memory reference 
    def __repr__(self):     #representation
        return str(self.value)

#class for Integer tokens
class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

#class for Float tokens
class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)

#class for operations
class Operation(Token):
    def __init__(self, value):
        super().__init__("OP", value)

class Declaration(Token):
    def __init__(self, value):
        super().__init__("DEC", value)

class Variable(Token):
    def __init__(self, value):
        super().__init__("VAR", value)
