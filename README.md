# Moduler & Package – Multi-Utility Toolkit

**Author: Siddhi Gadhiya**

## 📌 Project Overview

**Moduler & Package – Multi-Utility Toolkit** is a menu-driven Python project that brings several useful utilities together in one program. The user selects an option from the main menu, and the program calls the relevant function from a custom module.

The project is organized as a Python package named `modules`. The main menu is in `main.py`, general utility operations are in `modules/operations.py`, and file-handling functions are in `modules/file_operations.py`.

## 🛠️ Technology Used

- Python 3.14.6
- Visual Studio Code (VS Code)
- Git
- GitHub

## 🎯 Objective

The objective of this project is to practise Python modules and packages by building a reusable, menu-driven toolkit. It demonstrates the following concepts that are present in the program:

- Importing built-in and custom modules
- Creating and calling user-defined functions
- Variables, strings, lists, and a dictionary
- Taking input and displaying output
- Type conversion with `int()` and `float()`
- Conditional statements and loops
- Date and time operations
- Mathematical calculations
- Random data generation
- UUID generation
- File creation, writing, reading, and appending
- Exploring module attributes with `dir()`

## 📂 Project Structure

```text
Moduler & Package/
│
├── main.py
├── README.md
├── output.png
├── example.txt
│
└── modules/
    ├── __init__.py
    ├── operations.py
    ├── file_operations.py
    │
    └── __pycache__/
        ├── __init__.cpython-314.pyc
        ├── operations.cpython-314.pyc
        └── file_operations.cpython-314.pyc
```

**Note:** `example.txt` is created when the File Operations menu is used. It is a runtime-created example file; it does not need to exist before the program is run. `output.png` contains screenshots of the program output.

## 📄 File Description

### `main.py`

- Displays the main menu.
- Gets the user's menu choice with `input()`.
- Uses `if`, `elif`, and `else` to decide which operation to run.
- Calls functions imported from the custom modules.
- Uses a `while` loop to keep showing the menu until the user selects Exit.

### `modules/__init__.py`

Contains a short comment describing the custom package. It is included in the `modules` package folder.

### `modules/operations.py`

Contains functions for:
- Date and time operations
- Mathematical calculations
- Random data generation
- UUID generation
- Exploring attributes of supported modules

It imports the built-in modules `datetime`, `time`, `math`, `random`, and `uuid`.

### `modules/file_operations.py`

Contains the file operations menu and functions to create a file, write data, read data, and append data. It uses `open()`, `write()`, `read()`, and `close()`.

### `example.txt`

A sample text file that can be created by choosing **File Operations → Create a new file**. The user can then write, read, or append text to it using the program.

### `output.png`

Contains the combined screenshot output for the project.

### `README.md`

Documents the project overview, features, structure, concepts used, instructions to run the program, and sample output.

## ✨ Features

### 1. Datetime and Time Operations

The Datetime and Time menu provides these options:

- Display the current date and time using `datetime.datetime.now()`
- Calculate the number of days between two dates
- Format a date from `YYYY-MM-DD` to `DD-MM-YYYY`
- Measure elapsed time with a stopwatch
- Run a countdown timer

The code uses `strftime()` to format a date, `strptime()` to parse a date entered by the user, `time.time()` to measure elapsed time, and `time.sleep(1)` to pause the countdown for one second. The date difference uses `.days` and `abs()`.

### 2. Mathematical Operations

The Mathematical Operations menu includes:

- Calculate a number's factorial with `math.factorial()`
- Calculate the compound amount from a principal, rate, and time
- Calculate sine, cosine, and tangent for an angle entered in degrees
- Calculate the area of a circle, rectangle, or triangle

The code uses `math.radians()` to convert degrees to radians, `math.sin()`, `math.cos()`, and `math.tan()` for trigonometry, and `math.pi` for the circle area. It uses `round()` to display rounded results and `format(amount, ".2f")` to show the amount with two decimal places.

### 3. Random Data Generation

The Random Data Generation menu can:

- Generate a random integer from 1 to 100
- Create a list containing random integers
- Generate a password from letters, digits, and selected symbols
- Generate a six-digit random OTP-style number

The code uses `random.randint()` to generate random integers and `random.choice()` to choose a character for the password. A `for` loop builds the random list and password.

### 4. Unique Identifier Generation

The UID option uses `uuid.uuid4()` to generate and display a UUID. The generated value is an identifier string in a UUID format.

### 5. File Operations

The File Operations menu provides four actions:

- **Create a new file:** Opens the entered file name in append mode (`"a"`), which creates the file if it does not already exist.
- **Write to a file:** Opens the file in write mode (`"w"`) and writes the entered text. Write mode replaces existing content.
- **Read from a file:** Opens the file in read mode (`"r"`) and displays its contents.
- **Append to a file:** Opens the file in append mode (`"a"`) and writes additional text at the end.

The code explicitly closes each file with `close()`. For example, the user can create `example.txt`, write `This is a sample file.`, and read that text back from the file.

### 6. Explore Module Attributes

The module exploration option accepts a module name from this set: `datetime`, `time`, `math`, `random`, and `uuid`. A dictionary maps each supported name to its imported module object. The program checks whether the entered name exists in the dictionary and, if it does, uses `dir()` to display the module's available names.

## 📚 Concepts Used

The following concepts are used in the supplied code.

### Python Basics

- Variables for storing choices, dates, numbers, text, and calculation results
- Strings for menu choices, prompts, dates, file names, and messages
- Lists for storing generated random numbers
- Dictionary for mapping supported module names to module objects
- `input()` for user input
- `print()` for output
- `int()` and `float()` for converting input values
- String concatenation with `+`
- `round()`, `abs()`, and `format()`

### Conditional Statements

- `if`
- `elif`
- `else`
- Membership checking with `in`

### Loops and Flow Control

- `while True` for repeating menus
- `while seconds > 0` for the countdown
- `for` loops for building lists and passwords
- `break` to leave a menu loop

### Functions

- Defining functions with `def`
- Calling functions from the main program
- Separating each feature into its own function

### Modules and Packages

- `import`
- Importing selected functions with `from ... import`
- Built-in modules: `datetime`, `time`, `math`, `random`, `uuid`
- Custom modules: `operations.py` and `file_operations.py`
- Package folder: `modules/`
- `__init__.py`

### Date and Time Functions

- `datetime.datetime.now()`
- `strftime()`
- `strptime()`
- `time.time()`
- `time.sleep()`
- Date subtraction and `.days`

### Mathematical Functions

- `math.factorial()`
- `math.radians()`
- `math.sin()`
- `math.cos()`
- `math.tan()`
- `math.pi`

### Random and UUID Functions

- `random.randint()`
- `random.choice()`
- `uuid.uuid4()`

### File Handling

- `open()`
- `write()`
- `read()`
- `close()`
- File modes: `"a"`, `"w"`, and `"r"`

### Module Exploration

- Dictionary lookup
- Membership checking with `in`
- `dir()` to list module attributes

## ▶️ How to Run

1. Open the `Moduler & Package` folder in VS Code.
2. Open the terminal in that folder.
3. Run this command:

```bash
python main.py
```

4. Choose an option by entering its number.
5. Follow the prompts shown in the terminal.
6. Choose **Exit** from the main menu to close the program.

## 🖥️ Sample Output

```text

Welcome to Multi-Utility Toolkit 

Choose an option: 

1. Datetime and Time Operations 

2. Mathematical Operations 

3. Random Data Generation 

4. Generate Unique Identifiers (UID) 

5. File Operations (Custom Module) 

6. Explore Module Attributes (dir()) 

7. Exit 

Enter your choice: 1 

Datetime and Time Operations: 

1. Display current date and time 

2. Calculate difference between two dates/times 

3. Format date into custom format 

4. Stopwatch 

5. Countdown Timer 

6. Back to Main Menu 

Enter your choice: 1 

Current Date and Time: 2026-10-07 16:12:19 

Datetime and Time Operations: 

1. Display current date and time 

2. Calculate difference between two dates/times 

3. Format date into custom format 

4. Stopwatch 

5. Countdown Timer 

6. Back to Main Menu 

Enter your choice: 2 

Enter the first date (YYYY-MM-DD): 2007-04-15 

Enter the second date (YYYY-MM-DD): 2006-12-19 

Difference: 117 days 

Datetime and Time Operations: 

1. Display current date and time 

2. Calculate difference between two dates/times 

3. Format date into custom format 

4. Stopwatch 

5. Countdown Timer 

6. Back to Main Menu 

Enter your choice: 6 

Welcome to Multi-Utility Toolkit 

Choose an option: 

1. Datetime and Time Operations 

2. Mathematical Operations 

3. Random Data Generation 

4. Generate Unique Identifiers (UID) 

5. File Operations (Custom Module) 

6. Explore Module Attributes (dir()) 

7. Exit 

Enter your choice: 2 

Mathematical Operations: 

1. Calculate Factorial 

2. Solve Compound Interest 

3. Trigonometric Calculations 

4. Area of Geometric Shapes 

5. Back to Main Menu 

Enter your choice: 1 

Enter a number: 5 

Factorial: 120 

Mathematical Operations: 

1. Calculate Factorial 

2. Solve Compound Interest 

3. Trigonometric Calculations 

4. Area of Geometric Shapes 

5. Back to Main Menu 

Enter your choice: 2 

Enter principal amount: 1000 

Enter rate of interest (in %): 5 

Enter time (in years): 2 

Compound Interest: 1102.50 

Mathematical Operations: 

1. Calculate Factorial 

2. Solve Compound Interest 

3. Trigonometric Calculations 

4. Area of Geometric Shapes 

5. Back to Main Menu 

Enter your choice: 5 

Welcome to Multi-Utility Toolkit 

Choose an option: 

1. Datetime and Time Operations 

2. Mathematical Operations 

3. Random Data Generation 

4. Generate Unique Identifiers (UID) 

5. File Operations (Custom Module) 

6. Explore Module Attributes (dir()) 

7. Exit 

Enter your choice: 3 

Random Data Generation: 

1. Generate Random Number 

2. Generate Random List 

3. Create Random Password 

4. Generate Random OTP 

5. Back to Main Menu 

Enter your choice: 3 

Enter password length: 8 

Generated Password: 8DZLXAkW 

Random Data Generation: 

1. Generate Random Number 

2. Generate Random List 

3. Create Random Password 

4. Generate Random OTP 

5. Back to Main Menu 

Enter your choice: 5 

Welcome to Multi-Utility Toolkit 

Choose an option: 

1. Datetime and Time Operations 

2. Mathematical Operations 

3. Random Data Generation 

4. Generate Unique Identifiers (UID) 

5. File Operations (Custom Module) 

6. Explore Module Attributes (dir()) 

7. Exit 

Enter your choice: 4 

Generate Unique Identifiers (UID): 

Generated UID: b5b4fe26-6d50-435c-8978-a44e8f10ec66 

Welcome to Multi-Utility Toolkit 

Choose an option: 

1. Datetime and Time Operations 

2. Mathematical Operations 

3. Random Data Generation 

4. Generate Unique Identifiers (UID) 

5. File Operations (Custom Module) 

6. Explore Module Attributes (dir()) 

7. Exit 

Enter your choice: 5 

File Operations: 

1. Create a new file 

2. Write to a file 

3. Read from a file 

4. Append to a file 

5. Back to Main Menu 

Enter your choice: 1 

Enter file name: example.txt 

File created successfully! 

File Operations: 

1. Create a new file 

2. Write to a file 

3. Read from a file 

4. Append to a file 

5. Back to Main Menu 

Enter your choice: 2 

Enter file name: example.txt 

Enter data to write: This is a sample file. 

Data written successfully! 

File Operations: 

1. Create a new file 

2. Write to a file 

3. Read from a file 

4. Append to a file 

5. Back to Main Menu 

Enter your choice: 3 

Enter file name: example.txt 

File Content: 

This is a sample file. 

File Operations: 

1. Create a new file 

2. Write to a file 

3. Read from a file 

4. Append to a file 

5. Back to Main Menu 

Enter your choice: 5 

Welcome to Multi-Utility Toolkit 

Choose an option: 

1. Datetime and Time Operations 

2. Mathematical Operations 

3. Random Data Generation 

4. Generate Unique Identifiers (UID) 

5. File Operations (Custom Module) 

6. Explore Module Attributes (dir()) 

7. Exit 

Enter your choice: 6 

Explore Module Attributes: 

Enter module name to explore: math 

Available Attributes in math module: 

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp'] 

Welcome to Multi-Utility Toolkit 

Choose an option: 

1. Datetime and Time Operations 

2. Mathematical Operations 

3. Random Data Generation 

4. Generate Unique Identifiers (UID) 

5. File Operations (Custom Module) 

6. Explore Module Attributes (dir()) 

7. Exit 

Enter your choice: 7 

Thank you for using Multi-Utility Toolkit!

```