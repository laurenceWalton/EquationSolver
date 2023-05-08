import ply.lex as lex
import ply.yacc as yacc

class EquationParser:
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

    @staticmethod
    def t_error(t):
        t.type = 'ILLEGAL'
        t.value = t.value[0]
        t.lexer.skip(1)
        return t

    # Build the lexer
    def build_lexer(self):
        self.lexer = lex.lex(module=self)

    # Equation
    def p_equation(self, p):
        """equation : expression '=' expression"""
        p[0] = (p[2], p[1], p[3])

    # Expression
    def p_expression_add(self, p):
        """expression : expression '+' term
                    | expression '-' term"""
        p[0] = (p[2], p[1], p[3])

    def p_expression_term(self, p):
        """expression : term"""
        p[0] = p[1]

    # Term
    def p_term_mul(self, p):
        """term : term '*' factor
                | term '/' factor"""
        p[0] = (p[2], p[1], p[3])

    def p_term_factor(self, p):
        """term : factor"""
        p[0] = p[1]

    # Factor
    def p_factor_number(self, p):
        """factor : NUMBER"""
        p[0] = float(p[1])

    def p_factor_variable(self, p):
        """factor : VARIABLE"""
        p[0] = ('variable', p[1])

    def p_factor_paren(self, p):
        """factor : '(' expression ')'"""
        p[0] = p[2]

    def p_factor_multiply_number_variable(self, p):
        """factor : NUMBER VARIABLE"""
        p[0] = ('*', float(p[1]), ('variable', p[2]))

    def p_expression_uminus(self, p):
        """expression : '-' term"""
        p[0] = ('*', p[2], -1.0)

    def p_factor_implicit_mul(self, p):
        """factor : factor '(' expression ')'"""
        p[0] = ('*', p[1], p[3])

    # Rule to handle syntax errors
    def p_error(self, p):
        print("Syntax error at '%s'" % p.value)

    def single_variable_error(self, parsed_equation):
        variables = set()

        def check_variables(parsed_equation):
            if isinstance(parsed_equation, tuple):
                if parsed_equation[0] == "variable":
                    variables.add(parsed_equation[1])
                else:
                    for sub_expression in parsed_equation[1:]:
                        check_variables(sub_expression)

        check_variables(parsed_equation)
        if len(variables) > 1:
            raise ValueError("Only a single variable is allowed")

    def __init__(self):
        self.build_lexer()
        self.parser = yacc.yacc(module=self, debug=False, write_tables=False)

    def parse(self, data):
        parsed_equation = self.parser.parse(data, lexer=self.lexer)
        self.single_variable_error(parsed_equation)
        return parsed_equation

