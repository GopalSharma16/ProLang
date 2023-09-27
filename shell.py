from my_lexer import Lexer
from my_parser import Parser
from my_interpreter import Interpreter

while True:
    #taking input 
    text = input("ProLang> ")
    if text == "exit":
        exit()
    else:
        #tokenizing the input
        tokenizer = Lexer(text)
        tokens = tokenizer.tokenize()
        print(tokens)
        
        #parsing the tokens
        parser = Parser(tokens)
        parse_tree = parser.parse()
        print(parse_tree)

        # #interpreting the parse tree
        # interpreter = Interpreter(parse_tree)
        # result = interpreter.interpret()

        # print(result)