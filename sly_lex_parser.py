# -----------------------------------------------------------------------------
# lex_parser.py
#
# (Python SLY Lex & Yacc)
# Analisis Lexico y Sintaxico
#
# Gustavo Vasquez
# A00823326
# -----------------------------------------------------------------------------

from sly import Lexer, Parser

# -----------------------------------------------------------------------------
# Lexer
# -----------------------------------------------------------------------------
class MyLexer(Lexer):
    tokens = {
        'PROGRAM',
        'VAR',
        'INT',
        'FLOAT',
        'PRINT',
        'IF',
        'ELSE',
        'ID',
        'CTEF',
        'CTEI',
        'CTESTRING',
        'LPAREN',
        'RPAREN',
        'LCURLY',
        'RCURLY',
        'SEMICOLON',
        'COLON',
        'COMMA',
        'EQUALS',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'GT',
        'LT',
        'NE',
    }
    ignore = ' \t'

    LPAREN = r'\('
    RPAREN = r'\)'
    LCURLY = r'\{'
    RCURLY = r'\}'
    SEMICOLON = r'\;'
    COLON = r'\:'
    COMMA = r'\,'
    EQUALS = r'\='
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    GT = r'\>'
    LT = r'\<'
    NE = r'\<>'

    CTESTRING = r'"[a-zA-Z0-9!@#$%^&*()]*"'
    ID = r'[a-zA-Z_][a-zA-Z_0-9]*'

    # Palabras Reservadas dentro de ID
    ID['if'] = 'IF'
    ID['else'] = 'ELSE'
    ID['program'] = 'PROGRAM'
    ID['var'] = 'VAR'
    ID['int'] = 'INT'
    ID['float'] = 'FLOAT'
    ID['print'] = 'PRINT'

    @_(r'[+-]?[0-9]*[.][0-9]+')
    def CTEF(self, t):
        t.value = float(t.value)
        return t

    @_(r'[+-]?[0-9]+')
    def CTEI(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

# -----------------------------------------------------------------------------
# Parser
# -----------------------------------------------------------------------------
class MyParser(Parser):
    tokens = MyLexer.tokens

    @_('PROGRAM ID SEMICOLON programB')
    def program(self, p):
        return p

    @_('vars bloque',
       'bloque')
    def programB(self, p):
        return p

    @_('VAR ID varsI COLON tipo SEMICOLON varsB')
    def vars(self, p):
        return p

    @_('COMMA ID varsI',
       'empty')
    def varsI(self, p):
        return p

    @_('ID varsI COLON tipo SEMICOLON varsB',
       'empty')
    def varsB(self, p):
        return p

    @_('INT',
       'FLOAT')
    def tipo(self, p):
        return p

    @_('LCURLY bloqueB RCURLY')
    def bloque(self, p):
        return p

    @_('estatuto bloqueB',
       'empty')
    def bloqueB(self, p):
        return p

    @_('asignacion',
       'condicion',
       'escritura')
    def estatuto(self, p):
        return p

    @_('ID EQUALS expresion SEMICOLON')
    def asignacion(self, p):
        return p

    @_('PRINT LPAREN escrituraB RPAREN SEMICOLON')
    def escritura(self, p):
        return p

    @_('expresion escrituraC',
       'CTESTRING escrituraC')
    def escrituraB(self, p):
        return p

    @_('COMMA escrituraB',
       'empty')
    def escrituraC(self, p):
        return p

    @_('exp expresionB')
    def expresion(self, p):
        return p

    @_('GT exp',
       'LT exp',
       'NE exp',
       'empty')
    def expresionB(self, p):
        return p

    @_('IF LPAREN expresion RPAREN bloque condicionB SEMICOLON')
    def condicion(self, p):
        return p

    @_('ELSE bloque',
       'empty')
    def condicionB(self, p):
        return p

    @_('termino expB')
    def exp(self, p):
        return p

    @_('PLUS exp',
       'MINUS exp',
       'empty')
    def expB(self, p):
        return p

    @_('factor terminoB')
    def termino(self, p):
        return p

    @_('TIMES termino',
       'DIVIDE termino',
       'empty')
    def terminoB(self, p):
        return p

    @_('LPAREN expresion RPAREN',
       'factorB varcte')
    def factor(self, p):
        return p

    @_('PLUS',
       'MINUS',
       'empty')
    def factorB(self, p):
        return p

    @_('ID',
       'CTEI',
       'CTEF')
    def varcte(self, p):
        return p

    @_(' ')
    def empty(self, p):
        return p

    def error(self, p):
        if p:
            print("Syntax error at token", p.type)
            self.tokens
        else:
            print("Syntax error at EOF")

if __name__ == '__main__':
    # Testing Lexer
    lexer = MyLexer()
    data = '"Gus" 3 + 2 ; , 2 ^ 8 - 2 if else print(2.0)'
    for tok in lexer.tokenize(data):
        print(tok)

    # Testing Parser
    parser = MyParser()
    try:
        file = open("test_yacc.txt", "r")
        for line in file:
            parser.parse(lexer.tokenize(line))
            print(f"approved line: {line}")
    except EOFError:
        print('ERROR')