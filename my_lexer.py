from my_tokens import *
class Lexer:
    
    #defining class variables
    digits = "0123456789"
    operations = "+-/*%"
    stopwords = [" "]

    #instantiation of the instance variables
    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.token = None
        self.tokens = []
        self.char = self.text[self.idx]

    #start the tokenization process
    def tokenize(self):
        while self.idx<len(self.text):
            #to identify integer
            if self.char in Lexer.digits:
                self.token = self.extract_num()

            #to identify float
            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move()

            #to identify stopwords like blank spaces 
            elif self.char in Lexer.stopwords:
                self.move()
                continue

            self.tokens.append(self.token)
        return self.tokens
    
    #to extract the numbers from the given input string
    def extract_num(self):
        number = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == '.') and (self.idx < len(self.text)):
            if self.char == '.':
                isFloat = True  
            number += self.char
            self.move()

        if isFloat == True:
            return Float(number)
        else:
            return Integer(number)
    
    #to increment the index 
    def move(self):
        self.idx += 1
        if self.idx<len(self.text):
            self.char = self.text[self.idx]
        