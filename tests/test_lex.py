# ------------------------------------------------------------
# test_lex.py
#
# (Python Lex & Yacc)
# Analisis Lexico - Pruebas
#
# Gustavo Vasquez
# A00823326
# ------------------------------------------------------------

from lex_yacc import MyLexer

PLYLexer = MyLexer()


# Probar IDs
def test_IDs() -> []:
    results = []
    test_ids = '''
        abcedfg
        mkd92842mdwka
        msms_ssdd_2983_222
    '''
    PLYLexer.input(test_ids)
    while True:
        tok = PLYLexer.token()
        if not tok:
            break
        results.append(tok)

    assert (len(results)) == 3
    # Comprobar que el tipo del Token sea ID
    for result in results:
        assert result.type == 'ID'
    return results


# Probar Numeros
def test_numbers() -> []:
    results = []
    test_numbers = '''
        10
        100
        -92838
        +678
    '''
    PLYLexer.input(test_numbers)
    while True:
        tok = PLYLexer.token()
        if not tok:
            break
        results.append(tok)

    assert (len(results)) == 4
    # Comprobar que el tipo del Token sea CTEI
    for result in results:
        assert result.type == 'CTEI'
    return results


# Probar Decimales
def test_floats() -> []:
    results = []
    test_floats = '''
        0.0
        3.45
        -45.67754334
    '''
    PLYLexer.input(test_floats)
    while True:
        tok = PLYLexer.token()
        if not tok:
            break
        results.append(tok)

    assert (len(results)) == 3
    # Comprobar que el tipo del Token sea CTEF
    for result in results:
        assert result.type == 'CTEF'
    return results


# Probar Palabras Reservadas
def test_reserved() -> []:
    results = []
    test_reserved = '''
        if
        else
        print
        program
    '''
    PLYLexer.input(test_reserved)
    while True:
        tok = PLYLexer.token()
        if not tok:
            break
        results.append(tok)
    assert (len(results)) == 4
    assert results[0].type == 'IF'
    assert results[1].type == 'ELSE'
    assert results[2].type == 'PRINT'
    assert results[3].type == 'PROGRAM'
    return results


# Probar Simbolos
def test_operations() -> []:
    results = []
    test_operations = '''
        *
        +
        -
        /
    '''
    PLYLexer.input(test_operations)
    while True:
        tok = PLYLexer.token()
        if not tok:
            break
        results.append(tok)
    assert (len(results)) == 4
    assert results[0].type == 'TIMES'
    assert results[1].type == 'PLUS'
    assert results[2].type == 'MINUS'
    assert results[3].type == 'DIVIDE'
    return results


if __name__ == '__main__':
    tests_results = test_IDs()
    tests_results += test_numbers()
    tests_results += test_floats()
    tests_results += test_reserved()
    tests_results += test_operations()
    print(tests_results)
