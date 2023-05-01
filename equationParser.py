import ply.lex as lex
import ply.yacc as yacc

# Token Types for Lexical Analysis
tokens = (
    'NUMBER',
    'VARIABLE',
)

# Regular expression rules to identify tokens
literals = ['+','-','/','*', '(', ')', '=']
t_NUMBER = r'\d+'
t_VARIABLE = r'[a-zA-Z]+'
t_ignore = ' \t'

def t_error(t):
    t.type = 'ILLEGAL'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

# Build the lexer
lexer = lex.lex()

# Equation
def p_equation(p):
    """equation : expression '=' expression"""
    p[0] = ('equals', p[1], p[3])

# Expression
def p_expression_add(p):
    """expression : expression '+' term
                  | expression '-' term"""
    p[0] = (p[2], p[1], p[3])

def p_expression_term(p):
    """expression : term"""
    p[0] = p[1]

# Term
def p_term_mul(p):
    """term : term '*' factor
            | term '/' factor"""
    p[0] = (p[2], p[1], p[3])

def p_term_factor(p):
    """term : factor"""
    p[0] = p[1]

# Factor
def p_factor_number(p):
    """factor : NUMBER"""
    p[0] = float(p[1])

def p_factor_variable(p):
    """factor : VARIABLE"""
    p[0] = ('variable', p[1])

def p_factor_paren(p):
    """factor : '(' expression ')'"""
    p[0] = p[2]

def p_factor_multiply_number_variable(p):
    """factor : NUMBER VARIABLE"""
    p[0] = ('multiply', float(p[1]), ('variable', p[2]))

def p_expression_uminus(p):
    """expression : '-' term"""
    p[0] = ('uminus', p[2])

def p_factor_implicit_mul(p):
    """factor : factor '(' expression ')'"""
    p[0] = ('multiply', p[1], p[3])


# Rule to handle syntax errors
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the parser
parser = yacc.yacc(debug=False, write_tables=False)

# # Test parsing (uncomment to test, or run tests.py to run more parsing tests)
# equation = "2(x) = 24"
# parsed = parser.parse(equation)
# print(parsed)