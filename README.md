# Multi-Utility Toolkit-Moduler&Package

## Author:
👩‍💻 **Drashti Vasani**

---

## 📌 Project Overview

**Multi-Utility Toolkit** is a Python-based menu-driven program that combines several useful utilities into one application.

The program provides options:

* Date and time operations
* Mathematical calculations
* Random data generation
* UUID generation
* File operations
* Exploring module attributes using `dir()`

---

## 🚀 Features

### 1. Datetime and Time Operations

The datetime section provides the following utilities:

* 1. Display current date and time
* 2. Calculate the difference between two dates
* 3. Format a date into a custom format
* 4. Stopwatch
* 5. Countdown timer
* 6. Return to the main menu

The program uses Python's `datetime` and `time` modules for these operations.

---

### 2. Mathematical Operations

The mathematical section includes:

* 1. Factorial calculation
* 2. Compound interest calculation
* 3. Trigonometric calculations
* 4. Area of geometric shapes
* 5. Return to the main menu

For geometric areas, the program supports:

* Circle
* Rectangle
* Triangle

The program uses Python's `math` module for mathematical calculations.

---

### 3. Random Data Generation

The random data section provides:

* 1. Generate a random number
* 2. Generate a random list
* 3. Create a random password
* 4. Generate a random OTP
* 5. Random sampling
* 6. Return to the main menu

The password generator can use:

* Lowercase letters
* Uppercase letters
* Numbers
* Special characters

The program uses Python's `random` module.

---

### 4. Generate Unique Identifiers (UUID)

This option generates a unique UUID using Python's `uuid.uuid4()` function.

* Example format:
* Generated UUID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

### 5. File Operations

The file operations section provides:

* Create a new file
* Write data to a file
* Read data from a file
* Append data to a file
* Return to the main menu

* The application uses Python's built-in file handling with `open()`.

### 6. Explore Module Attributes

This feature allows the user to enter a module name and inspect its available attributes.

It uses:

* `__import__()`

* `dir()`

The program displays the attributes returned by `dir()`.

## 📁 Project Structure

The project contains the main Python program, a text file, output image, README file, and custom modules.

```text
Moduler&Packager/

│

├── main.py

├── modeler.txt

├── moduler&package.png

├── README.md

│

└── Moduler_Package/

    ├── __init__.py

    ├── file_operator.py

    └── math_operator.py
```

main.py contains the main menu and the datetime, random, UUID, file, and module-exploration functionality. The code also imports file_operator and math_operator from Module_Package.

## 🛠️ Technologies Used
* Python
* datetime
* time
* math
* random
* uuid
* os
Custom Python package: Module_Package


## ▶️ How to Run
* Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation with:

python --version

* Step 2: Open the project folder

Open the project in VS Code or a terminal.

* Step 3: Run the program
python main.py

* Step 4: Select an option

The main menu displays:

Welcome to Multi-Utility Toolkit

* Choose an option:

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit

Enter the number of the operation you want to use.

## 📋 Sample Output
```text
==============================
Welcome to Multi-Utility Toolkit
==============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
Enter your choice: 1

--- Datetime and Time Operations ---
1. Display current date and time
2. Calculate difference between two dates
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
Enter your choice: 1
Current Date and Time: 2026-10-06 21:04:44

--- Datetime and Time Operations ---
1. Display current date and time
2. Calculate difference between two dates
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
Enter your choice: 2
Enter the first date (YYYY-MM-DD): 2026-2-2
Enter the second date (YYYY-MM-DD): 2026-2-3
Difference: 1 days

--- Datetime and Time Operations ---
1. Display current date and time
2. Calculate difference between two dates
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
Enter your choice: 3
Enter date (YYYY-MM-DD): 2026-2-2
Formatted Date: 02-02-2026
Day: Monday
Month: February

--- Datetime and Time Operations ---
1. Display current date and time
2. Calculate difference between two dates
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
Enter your choice: 4
Stopwatch started. Press Enter to stop.

Elapsed Time: 2.24 seconds

--- Datetime and Time Operations ---
1. Display current date and time
2. Calculate difference between two dates
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
Enter your choice: 5
Enter countdown time in seconds: 2
Time remaining: 1 seconds
Time's up!

--- Datetime and Time Operations ---
1. Display current date and time
2. Calculate difference between two dates
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
Enter your choice: 6

==============================
Welcome to Multi-Utility Toolkit
==============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
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

Enter principal amount: 100
Enter rate of interest (in %): 10
Enter time (in years): 2006
Compound Interest: 10807529444041043966575105343021136479983711623440899627484265348921930551553352007680.00

Mathematical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu
Enter your choice: 3

Enter angle in degrees: 12
Sin(12.0): 0.2079
Cos(12.0): 0.9781
Tan(12.0): 0.2126

Mathematical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu
Enter your choice: 4

Area of Geometric Shapes:
1. Circle
2. Rectangle
3. Triangle
Enter your choice: 1
Enter radius: 12
Area of Circle: 452.39

Mathematical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu
Enter your choice: 5
==============================
 Welcome to Multi-Utility Toolkit
==============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
Enter your choice: 3

--- Random Data Generation ---
1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Random Sampling
6. Back to Main Menu
Enter your choice: 1
Random Number: 79

--- Random Data Generation ---
1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Random Sampling
6. Back to Main Menu
Enter your choice: 2
Random List: [16, 69, 94, 68, 16]

--- Random Data Generation ---
1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Random Sampling
6. Back to Main Menu
Enter your choice: 3
Enter password length: 5
Generated Password: !dxn0

--- Random Data Generation ---
1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Random Sampling
6. Back to Main Menu
Enter your choice: 4
Generated OTP: 548638

--- Random Data Generation ---
1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Random Sampling
6. Back to Main Menu
Enter your choice: 5
Enter items separated by commas: apple,banana
How many items to sample? 2
Random Sample: apple,banana

--- Random Data Generation ---
1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Random Sampling
6. Back to Main Menu
Enter your choice: 6

==============================
Welcome to Multi-Utility Toolkit
==============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
Enter your choice: 4

--- Generate Unique Identifiers (UUID) ---
Generated UUID: 67d59cef-aebd-4ed8-8dee-ad20adac1ff6

==============================
Welcome to Multi-Utility Toolkit
==============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
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

Enter file name: db.txt
File created successfully!

File Operations:
1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu
Enter your choice: 2

Enter file name: db.txt
Enter data to write: I AM LEARN TO PYTHON
Data written successfully!

File Operations:
1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu
Enter your choice: 3

Enter file name: db.txt
File Content:
I AM LEARN TO PYTHON

File Operations:
1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu
Enter your choice: 4

Enter file name: db.txt
Enter data to append: I AM LEARN TO PYTHON
Data appended successfully!

File Operations:
1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu
Enter your choice: 5

==============================
Welcome to Multi-Utility Toolkit
==============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
Enter your choice: 6

Explore Module Attributes:
Enter module name to explore: datetime
Available Attributes in datetime module:
['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

==============================
Welcome to Multi-Utility Toolkit
==============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
Enter your choice: 7

==============================
Thank you for using the Multi-Utility Toolkit!
==============================
```
## ⚠️ Error Handling

The program includes handling for several common input errors, including:

* Invalid date format
* Invalid numeric input
* Negative countdown values
* Invalid password length
* Invalid random sampling size
* Existing files
* Missing files
* Missing modules
* Invalid menu choices

## 🎯 Purpose of the Project

This project demonstrates the use of:
* Python built-in modules
* Functions
* Loops
* Conditional statements
* Exception handling
* User input
* File handling
* Random data generation
* UUID generation
* Python packages and custom modules
* Dynamic module importing
* dir() for exploring module attributes
#   M o d u l e r _ P a c k a g e  
 #   M o d u l e r - P a c k a g e  
 