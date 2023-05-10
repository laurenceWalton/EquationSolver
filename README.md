# Basic Equation Solver

A web application that allows users to input a simple equation and receive step-by-step instructions on how to solve it. The application uses PLY for parsing, GPT-3.5 Turbo (ChatGPT) for evaluation, and Flask for the frontend. An online version is available [here](your-ec2-link).

## How It Works

### Parsing Equations

The application uses PLY (Python implementation of lex/yacc) to parse simple math equations into a tuple form (e.g., "-2 + 2x = 4" => ('=', ('+', ('*', 2.0, -1.0), ('*', 2.0, ('variable', 'x'))), 4.0)). This ensures the equations adhere to syntactic and semantic requirements.

### Evaluating Expressions

To evaluate the expression (solve for the variable), a single GPT-3.5 Turbo (ChatGPT) API call is used. The prompt is two-shot (two examples of desired behavior) and performs quite well in limited testing. To run the application locally, an OpenAI API key is required.

### Frontend

Flask is used to create the basic application frontend, and an online version is hosted on AWS EC2.

## Run Locally

### Requirements

- Python 3
- Flask
- OpenAI

### 1. Create a virtual environment

```
python -m venv venv
```

### 2. Activate the virtual environment

Activate the virtual environment:

For Windows:

```
venv\Scripts\activate
```

For macOS and Linux:

```
source venv/bin/activate
```

### 3. Install Flask

With the virtual environment activated, install Flask and OpenAI API:

```
pip install Flask 
pip install openai 
pip install ply
```

### 4. Add OpenAI API Key

In the EquationEvaluator class, in equation_evaluator.py file

### 5. Run the application

Start the Flask development server:

```
flask run
```

By default, the application will be available at `http://127.0.0.1:5000/`.

### 6. Deactivate the virtual environment

When you're done working with the project, deactivate the virtual environment:

```
deactivate
```