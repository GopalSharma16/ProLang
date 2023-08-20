from my_lexer import Lexer
from my_parser import Parser

while True:
    text = input("ProLang> ")
    tokenizer = Lexer(text)
    my_tokens = tokenizer.tokenize()
    
    parser = Parser(my_tokens)
    parse_tree = parser.parse()

    print(parse_tree)