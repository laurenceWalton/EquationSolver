import openai

class EquationEvaluator:
    def __init__(self, parser):
        self.parser = parser
        
    def solve_parsed_equation(self, equation_tuple):

        # Add API key here
        openai.api_key = "YOUR_API_KEY"
        
        prompt = """
        Extract the simple equation from the following examples and return step-by-step solutions on how to solve them. The examples consist of the equation in tuple form, with the following possibilities for the first index of each: ['+','-','/','*', ‘=‘, ‘variable’].
            Example:
            ('=', ('+', ('*', 2.0, ('+', ('*', 4.0, ('variable', 'x')), 3.0)), 6.0), ('-', 24.0, ('*', 4.0, ('variable', 'x'))))
            Response:
            1. Start by sharing 2 with the numbers inside the bracket: (8x + 6) + 6 = 24 - 4x
            2. Add the numbers together and put them in a neat order: 8x + 12 = -4x + 24
            3. Move the numbers around to solve for x: 12x = 12
            4. Finally, find the value of x by dividing both sides by 12: x = 1

            Example:
            ('=', ('*', ('*', 4.0, ('variable', 'y')), -1.0), ('*', 20.0, -1.0))
            Response:
            1. Divide both sides by -4, and then you are left with y = 5

            Example:\n
        """
        parsed_equation_str = str(equation_tuple)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                },
                {
                    "role": "user",
                    "content": parsed_equation_str,
                },
            ],
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        
        return response['choices'][0]['message']['content']
    
    def evaluate(self, equation):
        parsed_equation = self.parser.parse(equation)
        solution = self.solve_parsed_equation(parsed_equation)
        return solution