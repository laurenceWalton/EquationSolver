# Basic Equation Solver

Parsing of simple maths equations (single variable, see below for examples) and then a very evaluation method using a GPT API call. Parsing done using PLY (Python implementation of Lex/Yacc).

## Requirements

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

### 4. Run the application

Start the Flask development server:

```
flask run
```

By default, the application will be available at `http://127.0.0.1:5000/`.

### 5. Deactivate the virtual environment

When you're done working with the project, deactivate the virtual environment:

```
deactivate
```