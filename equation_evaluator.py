class EquationEvaluator:
    def __init__(self, parser):
        self.parser = parser

    def evaluate(self, equation):
        parsed_equation = self.parser.parse(equation)
        # TODO: Implement equation evaluation
        return parsed_equation