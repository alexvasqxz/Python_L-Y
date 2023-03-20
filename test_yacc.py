# ------------------------------------------------------------
# test_yacc.py
#
# (Python Lex & Yacc)
# Analisis Sintaxico - Pruebas
#
# Gustavo Vasquez
# A00823326
# ------------------------------------------------------------

from lex_yacc import MyLexer
from lex_yacc import MyParser

lexer = MyLexer()
parser = MyParser()

try:
    file = open("test_yacc.txt", "r")
    for line in file:
        parser.parse(line)
        print(f"approved line: {line}")
except EOFError:
    print('ERROR')