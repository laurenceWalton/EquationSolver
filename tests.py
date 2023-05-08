from equation_parser import EquationParser
from equation_evaluator import EquationEvaluator

parser = EquationParser()
evaluator = EquationEvaluator(parser)

def test_runner_parse(test_cases):
    for i, (equation, expected_parsed) in enumerate(test_cases):
        parsed = parser.parse(equation)
        assert parsed == expected_parsed, f"Test {i + 1} failed: {equation} => Expected {expected_parsed}, got {parsed}"
        print(f"Test {i + 1} passed: {equation} => {parsed}")
        
def test_runner_eval(test_cases):
    for i, (equation, expected_solution) in enumerate(test_cases):
        solution = evaluator.evaluate(equation)
        assert solution == expected_solution, f"Test {i + 1} failed: {equation} => Expected {expected_solution}, got {solution}"
        print(f"Test {i + 1} passed: {equation} => {solution}")

# Test cases
test_cases_parsing = [
    ("7x - 2 = 21", ('=', ('-', ('*', 7.0, ('variable', 'x')), 2.0), 21.0)),
    ("2(4x + 3) + 6 = 24 -4x", ('=', ('+', ('*', 2.0, ('+', ('*', 4.0, ('variable', 'x')), 3.0)), 6.0), ('-', 24.0, ('*', 4.0, ('variable', 'x'))))),
    ("(2 - 6) = x - 3x", ('=', ('-', 2.0, 6.0), ('-', ('variable', 'x'), ('*', 3.0, ('variable', 'x'))))),
    ("5x - 10 = 15 + x", ('=', ('-', ('*', 5.0, ('variable', 'x')), 10.0), ('+', 15.0, ('variable', 'x')))),
    ("3(x - 2) = 6", ('=', ('*', 3.0, ('-', ('variable', 'x'), 2.0)), 6.0)),
    ("(x + 3) / 2 = 4", ('=', ('/', ('+', ('variable', 'x'), 3.0), 2.0), 4.0)),
    ("-4y = -20", ('=', ('*', ('*', 4.0, ('variable', 'y')), -1.0), ('*', 20.0, -1.0))),
    ("-2 + 2x = 4", ('=', ('+', ('*', 2.0, -1.0), ('*', 2.0, ('variable', 'x'))), 4.0)),
]

# test_cases_evaluation = [    
#     ("7x = 21", 3.0),    
#     ("2(4x + 3) + 6 = 24 -4x", -3.0),    
#     ("(2 - 6) = x - 3x", 2.0),    
#     ("5x - 10 = 15 + x", 2.5),    
#     ("3(x - 2) = 6", 4.0),    
#     ("(x + 3) / 2 = 4", 5.0),    
#     ("-4y = -20", 5.0),   
#     ("-2 + 2x = 4", 3.0),]

# Run the parsing tests
print("Running parsing tests...")
test_runner_parse(test_cases_parsing)

# # Run the evaluation tests 
# print("Running evaluation tests...")
# test_runner_eval(test_cases_evaluation)

