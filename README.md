# Moduler & Package – Multi-Utility Toolkit

************Author: Siddhi Gadhiya**********

********## 📌 Project Overview******

Moduler & Package is a Python-based ************Multi-Utility Toolkit********** that provides different useful operations through a menu-driven program.

The project is organized using a custom Python package named `modules`. Different operations are separated into individual Python files to make the project structured, reusable, and easy to understand.

********## 🛠️ Technology Used******

- Python 3.14.6

- VS Code

********## 🎯 Objective******

The main objective of this project is to implement and demonstrate:

- Python Modules and Packages

- Importing Modules

- Datetime and Time Operations

- Mathematical Operations

- Random Data Generation

- Unique Identifier Generation

- File Operations

- Dynamic Module Exploration using `dir()`

- Menu-driven programming

- Functions

- Variables

- Input and Output

- Conditional Statements

- Loops

- File Handling

********## 📂 Project Structure******

```text

Moduler & Package/

│

├── main.py

├── README.md

├── output.png

│

└── modules/

    ├── __init__.py

    ├── operations.py

    └── file_operations.py

```

********## 📄 File Description******

********### `main.py`******

Contains the main menu and connects all operations from the custom modules.

********### `modules/__init__.py`******

Used to initialize the custom `modules` package.

********### `modules/operations.py`******

Contains datetime/time, mathematical, random data, UUID, and module attribute operations.

********### `modules/file_operations.py`******

Contains file creation, writing, reading, and appending operations.

********### `README.md`******

Contains the complete project documentation.

********### `output.png`******

Contains the screenshot/image of the project output.

********## ✨ Features******

********### 1. Datetime and Time Operations******

- Display current date and time

- Calculate difference between two dates/times

- Format date into custom format

- Stopwatch

- Countdown Timer

Uses Python's `datetime` and `time` modules.

********### 2. Mathematical Operations******

- Factorial calculation

- Compound interest calculation

- Trigonometric calculations

- Area of geometric shapes

Shapes include Circle, Rectangle, and Triangle.

Uses Python's `math` module.

********### 3. Random Data Generation******

- Random number

- Random list

- Random password

- Random OTP

Uses Python's `random` module.

********### 4. Unique Identifier Generation******

Generates a unique identifier using Python's `uuid` module.

********### 5. File Operations******

- Create a new file

- Write data to a file

- Read file contents

- Append data to a file

File modes used:

- `r` – Read

- `w` – Write

- `a` – Append

********### 6. Explore Module Attributes******

Uses Python's built-in `dir()` function to display available attributes of supported modules:

- `datetime`

- `time`

- `math`

- `random`

- `uuid`

********## 📚 Concepts Used******

********### Python Basics******

- Variables

- Data Types

- Input

- Output

- Type Conversion

- Strings

- Lists

- Dictionary

********### Conditional Statements******

- `if`

- `elif`

- `else`

********### Loops******

- `while`

- `for`

- `break`

********### Functions******

- User-defined functions

- Function calling





********### Modules and Packages******

- `import`

- Built-in modules

- Custom modules

- Custom package using `modules/`

- `__init__.py`

********### File Handling******

- `open()`

- `read()`

- `write()`

- `close()`

- File modes `r`, `w`, `a`

********### Other Python Concepts******

- `datetime.now()`

- `strftime()`

- `strptime()`

- `time.time()`

- `time.sleep()`

- `math.factorial()`

- `math.sin()`

- `math.cos()`

- `math.tan()`

- `math.pi`

- `random.randint()`

- `random.choice()`

- `uuid.uuid4()`

- `dir()`

- String operations

- Type conversion

********## ▶️ How to Run******

1. Open the `Moduler & Package` folder in VS Code.

2. Open the terminal.

3. Run:

```bash

python main.py

```

4. The program will display the main menu.

5. Select an option by entering the corresponding number.

********## 🖥️ Sample Output******

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

['\\\_\\\_doc\\\_\\\_', '\\\_\\\_loader\\\_\\\_', '\\\_\\\_name\\\_\\\_', '\\\_\\\_package\\\_\\\_', '\\\_\\\_spec\\\_\\\_', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp'] 

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
