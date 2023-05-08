from flask import Flask, request, render_template
from equation_parser import EquationParser
from equation_evaluator import EquationEvaluator

app = Flask(__name__)

# Initialize the parser and evaluator
parser = EquationParser()
evaluator = EquationEvaluator(parser)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        
        steps = evaluator.evaluate(text)

        return render_template('index.html', result=str(steps), input_text=text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
