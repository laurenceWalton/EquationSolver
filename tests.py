from eqsolver import parser

def test_runner(test_cases):
    for i, (equation, expected_parsed) in enumerate(test_cases):
        parsed = parser.parse(equation)
        assert parsed == expected_parsed, f"Test {i + 1} failed: {equation} => Expected {expected_parsed}, got {parsed}"
        print(f"Test {i + 1} passed: {equation} => {parsed}")

# Test cases
test_cases_parsing = [
    ("7x - 2 = 21", ('equals', ('-', ('multiply', 7.0, ('variable', 'x')), 2.0), 21.0)),
    ("2(4x + 3) + 6 = 24 -4x", ('equals', ('+', ('multiply', 2.0, ('+', ('multiply', 4.0, ('variable', 'x')), 3.0)), 6.0), ('-', 24.0, ('multiply', 4.0, ('variable', 'x'))))),
    ("(2 - 6) = x - 3x", ('equals', ('-', 2.0, 6.0), ('-', ('variable', 'x'), ('multiply', 3.0, ('variable', 'x'))))),
    ("5x - 10 = 15 + x", ('equals', ('-', ('multiply', 5.0, ('variable', 'x')), 10.0), ('+', 15.0, ('variable', 'x')))),
    ("3(x - 2) = 6", ('equals', ('multiply', 3.0, ('-', ('variable', 'x'), 2.0)), 6.0)),
    ("(x + 3) / 2 = 4", ('equals', ('/', ('+', ('variable', 'x'), 3.0), 2.0), 4.0)),
    ("-4y = -20", ('equals', ('uminus', ('multiply', 4.0, ('variable', 'y'))), ('uminus', 20.0))),
]

# Run the parsing tests - no equation evaluation yet
test_runner(test_cases_parsing)

