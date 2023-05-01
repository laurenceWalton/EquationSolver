from flask import Flask, request, render_template
from equationParser import parser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        parsed = parser.parse(text)
        return render_template('index.html', result=str(parsed), input_text=text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
