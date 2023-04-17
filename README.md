# Python Lex and Yacc
Python Lexical and Syntax Analysis
Main characteristics to be implemented and tested
<ul>
<li>A Lexical Analysis using Lex for Token Recognition </li>
<li>Some tokens will include IDs, reserved words, operation symbols </li>
<li>Some tokens will be recognized using Regular Expressions</li>
<li>A Syntax Analysis using grammars for Expression Recognition</li>
<li>The grammars will use either other expressions or the already created tokens from the Lexical Analysis</li>
<li>Working together, the Lexical and Syntax Analysis will Parse complex expressions step by step and create the Parse Table</li>
</ul>

## Files in this Repo

### lex_yacc.py
This file contains both the Lex and Yacc Analysis. The first part with all of the tokens and regular expressions for more complex tokens such as numbers, floating numbers, ids, and strings.
The second part of the file contains the grammars used for recognizing expressions and building the parser.

### test_lex.py
This file has unit tests for the Lexical Analysis part of the previous file, testing IDs, numbers, floating numbers, operation symbols, and reserved words, making sure that the first part of the Parser (Lex) is working properly.

### test_yacc.py
This file tests the second part of the Analysis (Yacc) to make sure that the parsetab is created successfully, by testing the parser with expressions from the test_yacc.txt file.

### test_yacc.txt
This text file contains the lines that will be used in the test_yacc.py file, with examples from simple to more complex, following the structure we have in the diagrams for the expressions.

### sly_lex_yacc.txt
This file contains a lexer and a parser implementation in SLY rather than PLY, it has an test example for the lexer and it uses the same file for testing the parser than the PLY one (test_yacc.txt).

## Evidence of Accepted Tests

### Lexical Tests
![alt text](https://github.com/alexvasqxz/Python_Lex_and_Yacc/blob/main/images/test_lex_1.png)

### Syntax Tests
![alt text](https://github.com/alexvasqxz/Python_Lex_and_Yacc/blob/main/images/test_yacc_1.png)
