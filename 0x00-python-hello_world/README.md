0x00. Python - Hello, World
How to use the Python interpreter:

The Python interpreter is a command-line tool that allows you to interact with Python directly. To use it:

    Open a Terminal or Command Prompt:
    Open the terminal on your system.

    Type python or python3:
    Simply typing python or python3 (depending on your system) and pressing Enter will launch the Python interpreter.

    Interact with Python:
    You can now enter Python code directly into the interpreter prompt. For example:

    python

    print("Hello, Python!")

    Exit the Interpreter:
    To exit the interpreter, you can type exit() or press Ctrl + D (or Cmd + D on macOS).

How to print text and variables using print:

The print function in Python is used to display text or variables. Examples:

python

# Print a string
print("Hello, Python!")

# Print variables
name = "John"
age = 25
print("Name:", name, "Age:", age)

# Formatted string
print(f"Name: {name}, Age: {age}")

How to use strings:

Strings in Python are sequences of characters. You can create strings using single (') or double (") quotes. Examples:

python

# Single-line string
message = 'This is a string.'

# Multi-line string
multiline_string = """This is
a multi-line
string."""

You can perform various operations on strings, such as concatenation, slicing, and formatting.
What are indexing and slicing in Python:

Indexing:
In Python, indexing starts at 0. You can access individual elements in a sequence (like a string) using their index.

python

text = "Python"
first_letter = text[0]  # 'P'
second_letter = text[1]  # 'y'

Slicing:
Slicing allows you to extract a portion of a sequence. It follows the syntax [start:stop:step].

python

text = "Python"
substring = text[0:3]  # 'Pyt'

