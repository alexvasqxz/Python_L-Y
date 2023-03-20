# ------------------------------------------------------------
# lex_yacc.py
#
# (Python Lex & Yacc)
# Analisis Lexico
#
# Gustavo Vasquez
# A00823326
# ------------------------------------------------------------

import ply.lex as lex
import ply.yacc as yacc

# Lista de Palabras Reservadas
reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
}

# Lista de TOKENS
tokens = [
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
] + list(reserved.values())


def MyLexer():
    # Expresiones Regulares para TOKENS Sencillos
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LCURLY = r'\{'
    t_RCURLY = r'\}'
    t_SEMICOLON = r'\;'
    t_COLON = r'\:'
    t_COMMA = r'\,'
    t_EQUALS = r'\='
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_GT = r'\>'
    t_LT = r'\<'
    t_NE = r'\<>'

    # Expresion Regular para ID
    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'ID')  # Revisa Palabras Reservadas
        return t

    # Expresion Regular para Decimales
    # Colocar antes que NUMBER
    def t_CTEF(t):
        r'[+-]?[0-9]*[.][0-9]+'
        t.value = float(t.value)
        return t

    # Expresion Regular para Numeros Enteros
    def t_CTEI(t):
        r'[+-]?[0-9]+'
        t.value = int(t.value)
        return t

    # Expresion Regular para Strings
    def t_CTESTRING(t):
        r'"[a-zA-Z0-9!@#$%^&*()]*"'
        t.type = 'CTESTRING'
        return t

    def t_newline(t):
        r'\n+'

    # Se ignoran espacios en blanco
    t_ignore = ' \t'

    # Error handling
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Consturye el Analizador Lexico
    return lex.lex()


# ------------------------------------------------------------
# lex_yacc.py
#
# (Python Lex & Yacc)
# Analisis Sintaxico
#
# Gustavo Vasquez
# A00823326
# ------------------------------------------------------------

def MyParser():
    def p_program(p):
        '''
        program : PROGRAM ID SEMICOLON programB
        programB : vars bloque
                 | bloque
        '''
        p[0] = None

    def p_vars(p):
        '''
        vars : VAR ID varsI COLON tipo SEMICOLON varsB
        varsI : COMMA ID varsI
              | empty
        varsB : ID varsI COLON tipo SEMICOLON varsB
              | empty
        '''
        p[0] = None

    def p_tipo(p):
        '''
        tipo : INT
             | FLOAT
        '''
        p[0] = None

    def p_bloque(p):
        '''
        bloque : LCURLY bloqueB RCURLY
        bloqueB : estatuto bloqueB
                | empty
        '''
        p[0] = None

    def p_estatuto(p):
        '''
        estatuto : asignacion
                 | condicion
                 | escritura
        '''
        p[0] = None

    def p_asignacion(p):
        '''
        asignacion : ID EQUALS expresion SEMICOLON
        '''
        p[0] = None

    def p_escritura(p):
        '''
        escritura : PRINT LPAREN escrituraB RPAREN SEMICOLON
        escrituraB : expresion escrituraC
                   | CTESTRING escrituraC
        escrituraC : COMMA escrituraB
                   | empty
        '''
        p[0] = None

    def p_expresion(p):
        '''
        expresion : exp expresionB
        expresionB : GT exp
                   | LT exp
                   | NE exp
                   | empty
        '''
        p[0] = None

    def p_condicion(p):
        '''
        condicion : IF LPAREN expresion RPAREN bloque condicionB SEMICOLON
        condicionB : ELSE bloque
                   | empty
        '''
        p[0] = None

    def p_exp(p):
        '''
        exp : termino expB
        expB : PLUS exp
             | MINUS exp
             | empty
        '''
        p[0] = None

    def p_termino(p):
        '''
        termino : factor terminoB
        terminoB : TIMES termino
                 | DIVIDE termino
                 | empty
        '''
        p[0] = None

    def p_factor(p):
        '''
        factor : LPAREN expresion RPAREN
               | factorB varcte
        factorB : PLUS
                | MINUS
                | empty
        '''
        p[0] = None

    def p_varcte(p):
        '''
        varcte : ID
               | CTEI
               | CTEF
        '''
        p[0] = None

    def p_empty(p):
        '''
        empty :
        '''
        p[0] = None

    def p_error(p):
        print("Syntax error at token", p.type)

    return yacc.yacc()
