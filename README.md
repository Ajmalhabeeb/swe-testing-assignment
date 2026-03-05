 Quick-Calc Calculator (Tkinter)

Quick-Calc is a simple calculator application developed in Python using the Tkinter GUI library. The application supports the four basic arithmetic operations: addition, subtraction, multiplication, and division. It also includes a Clear (C) button that resets the calculator display to **0**. Division by zero is handled gracefully by displaying an error instead of crashing the application.

The goal of this project is to demonstrate software engineering best practices such as **clean code structure, version control with Git, unit testing, integration testing, and professional documentation**.



# Project Structure
swe-testing-assignment
│
├── README.md
├── TESTING.md
├── pyproject.toml
│
├── src
│ └── quick_calc
│ ├── core.py
│ ├── gui.py
│ └── init.py
│
└── tests
├── test_core.py
└── test_integration_gui.py


- **core.py** → Contains the main calculation logic
- **gui.py** → Tkinter graphical interface
- **tests/** → Unit tests and integration tests


Setup Instructions
1. Clone the repository
git clone https://github.com/Ajmalhabeeb/swe-testing-assignment.git

cd swe-testing-assignment

2. Create a virtual environment
python -m venv .venv


Activate it (Windows):
..venv\Scripts\activate

3. Install dependencies
python -m pip install pytest


# Running the Calculator

To start the Tkinter calculator application:
$env:PYTHONPATH="src"; python -m quick_calc.gui


The calculator window will open and allow basic arithmetic operations.

Running Tests

The project uses **pytest** as the testing framework.

Run the complete test suite using one command:


python -m pytest


Example output:


collected 10 items
tests/test_core.py ......
tests/test_integration_gui.py ..
10 passed in 0.51s

Testing Framework Research
 Pytest vs Unittest

Python provides several testing frameworks, with **Unittest** and **Pytest** being two of the most commonly used.

Unittest is the built-in testing framework included in Python’s standard library. It follows the traditional xUnit style of testing and requires test classes and methods. While it is very stable and widely used, it often requires more boilerplate code and can be less readable for smaller projects.

Pytest is a modern and popular testing framework that focuses on simplicity and readability. Tests can be written as simple functions without requiring class structures. Pytest also provides powerful features such as fixtures, parameterized tests, detailed failure reports, and an extensive plugin ecosystem. Because of these features, pytest allows developers to write tests faster and maintain them more easily.

For this project, **pytest was selected** because it enables concise test writing, provides clearer output, and simplifies both unit testing and integration testing. This makes it ideal for small applications like Quick-Calc while still supporting professional testing practices.

Features

- Addition, subtraction, multiplication, and division
- Graceful handling of division by zero
- Clear (C) button resets the display to **0**
- Graphical user interface built with Tkinter
- Unit tests for core calculation logic
- Integration tests for GUI interaction
- Version control using Git and GitHub


# Version

Current release: **v1.0.0**

Initial version includes the calculator application, automated tests, and documentation

