from my_tokens import *
class Lexer:
    
    #defining class variables
    digits = "0123456789"
    operations = "+-/*%()="
    stopwords = [" "]
    letters = "abcdefghijklmnopqrstuvwxyz"
    declarations = ["create"]

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

            #to identify operation
            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move()

            #to identify stopwords like blank spaces 
            elif self.char in Lexer.stopwords:
                self.move()
                continue

            elif self.char in Lexer.letters:
                word = self.extract_word()

                #checking if the word is a reserved keyword or decleration
                if word in Lexer.declarations:
                    self.token = Declaration(word)
                
                #else it is a variable if is not a declaration
                else:
                    self.token = Variable(word)

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
    
    #to extract the words or alphabets from the given input string
    def extract_word(self):
        word = ""
        while(self.char in Lexer.letters and self.idx < len(self.text)):
            word += self.char
            self.move()
        return word

    #to increment the index 
    def move(self):
        self.idx += 1
        if self.idx<len(self.text):
            self.char = self.text[self.idx]