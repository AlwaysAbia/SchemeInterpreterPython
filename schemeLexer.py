from sly import Lexer
import re
import string

class schemeLexer(Lexer):
    ##Class that breaks down input string into tokens based on their regular expressions
    tokens = {LPAREN, RPAREN, NUMBER, ARITHMETIC, LOGIC,
              COMP, IF, LISP, LIST, LAMBDA, APPLEVAL, HELPERFUNC, DEFINE, STRING}

    ignore = ' \t'
    ignore_newline = r'\n+'
    ignore_comment = r'\#.*'

    LPAREN = r'\('
    RPAREN = r'\)'
    NUMBER = r'(-?\d+)(?:\.\d+)?'
    ARITHMETIC = r'\+|-|\*|/'
    LOGIC = r'\b(and|or)\b'
    COMP = r'(=|<|>)'
    IF = r'\bif\b'
    LISP = r'\b(car|cdr|cadr|cons|map|append)\b'
    LIST = r'\'\([^\)]*\)'
    LAMBDA = r'\blambda\b'
    APPLEVAL = r'\b(apply|eval)\b'
    HELPERFUNC = r'(null\?|length)'
    DEFINE = r'\bdefine\b'
    STRING = r'[a-zA-Z]+'

    def NUMBER(self, t):
        t.value = float(t.value)
        return t
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    def error(self, t):
        print("Invalid Character %s, Exiting Code" % t.value[1])
        exit()

##Test For me
if __name__ == '__main__':
    data = ''' (apply eval)
            '''
    lexer = schemeLexer()
    for tok in lexer.tokenize(data):
        print(tok)
    
