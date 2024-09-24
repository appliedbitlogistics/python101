# python101
A tutorial for teaching myself (and others) the Python programming language.

- John Haverlack
- Copyright (c) 2024 Applied Bit Logistics
- Version: 2024-09-23


My programming journey started the 1980's learning languages like [BASIC](https://en.wikipedia.org/wiki/BASIC), [Pascal](https://en.wikipedia.org/wiki/Pascal_(programming_language)), [Fortran](https://en.wikipedia.org/wiki/Fortran), [C](https://en.wikipedia.org/wiki/C_(programming_language)), [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic), [Assembly Language](https://en.wikipedia.org/wiki/Assembly_language) (x86), [Java](https://en.wikipedia.org/wiki/Java_(programming_language)), [BASH](https://en.wikipedia.org/wiki/Bash_(Unix_shell)), [HTML](https://en.wikipedia.org/wiki/HTML) [Perl](https://en.wikipedia.org/wiki/Perl), [PHP](https://en.wikipedia.org/wiki/PHP), [Javascript](https://en.wikipedia.org/wiki/JavaScript), and [Node.JS](https://en.wikipedia.org/wiki/Node.js). Since the 90's I've used several source code revision system like [RCS](https://en.wikipedia.org/wiki/Revision_Control_System), [CVS](https://en.wikipedia.org/wiki/Concurrent_Versions_System), [Subversion](https://en.wikipedia.org/wiki/Apache_Subversion), and [Git](https://en.wikipedia.org/wiki/Git) using a number of code editing software including [Emacs](https://en.wikipedia.org/wiki/Emacs), [Eclipse](https://en.wikipedia.org/wiki/Eclipse_(software)), [Atom](https://en.wikipedia.org/wiki/Atom_(text_editor)), [VS Code](https://en.wikipedia.org/wiki/Visual_Studio_Code), [VS Codium](https://vscodium.com/) on [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows), [Mac](https://en.wikipedia.org/wiki/MacOS), and [Linux](https://en.wikipedia.org/wiki/Linux) Operating systems on [X86](https://en.wikipedia.org/wiki/X86), [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family), [Motorolla 6811](https://en.wikipedia.org/wiki/Motorola_68HC11), [MIPS](https://en.wikipedia.org/wiki/MIPS_architecture) [RISC](https://en.wikipedia.org/wiki/R10000), [SPARC](https://en.wikipedia.org/wiki/SPARC), [Arduino](https://en.wikipedia.org/wiki/Arduino), and [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi) computer systems.

---

# Tutorial Outline

## [Introduction to Python Programming](https://chatgpt.com/share/66f2060a-2af0-8007-8520-387cc4954dd9)

While this tutorial aims to teach us how to program in Python, but the Python language is really just the lens through which we are learn how to program.  This tutorial is more about learning how to program than it is about Python.

> What is important is learning how to write code to process information.  Not the language we choose to use to do so.

This tutorial could just as easily be taught using any modern programming language, Node.JS, Rust, Go, etc.  Because of Python's popularity among the scientfic community it is a good choice as a practical (first) language to learn.

Because I've programmed in a number languages for many years, and I don't really know Python, my approach will be to outline the programming skills that progressively build previous skills in a language agnostic manner.  And then use Python to demonstrate these lessons.

> This tutorial will provide examples for Windows and Linux.  Programming on Macs is mostly similar to Linux but the installation and setup of your programming environment on Mac will be slighly different.

### Lesson 0: [Introduction & Setup](Lessons/00_Setup/lesson.md)

Before we jump into learning Python we need some skills and tools to help us.  We'll need to install **Python**, a **Code Editor**, a command line **terminal** shell, and **Git** at a minimum.  

### Lesson 1: [Hello World](Lessons/01_HelloWorld/lesson.md)

When learning any language it's traditionally to start with a very simple program that write the words "Hello World" to the screen.

### Lesson 2: Basic Syntax, Variables, and Data Types

**Objectives**:
- Python syntax and indentation.
- Variables, constants, and comments.
- Data types: integers, floats, strings, booleans.

Hands-on: Write a program that accepts user input, performs basic arithmetic, and prints the result.

## Core Python Programming Concepts

### Lesson 3: Operators and Expressions

**Objectives**:
- Arithmetic, comparison, logical, bitwise, and assignment operators.
- Operator precedence and expressions.

Hands-on: Write a calculator program that performs various operations.

### Lesson 4: Control Flow (Conditionals)

**Objectives**:
- If, elif, and else statements.
- Boolean logic and conditions.

Hands-on: Build a simple decision-making program, like a grading system based on user input.

### Lesson 5: Loops (for, while)

**Objectives**:
- For loops, while loops, and loop control (break, continue).
- Iterating over lists, strings, and ranges.

Hands-on: Create a number-guessing game with a loop and user input.

### Lesson 6: Functions and Modules

**Objectives**:
- Defining and calling functions.
- Function arguments and return values.
- Importing and using modules (math, random, etc.).

Hands-on: Write a function to check if a number is prime, and another that finds the greatest common divisor (GCD).

## Data Structures and Object-Oriented Programming

### Lesson 7: Lists, Tuples, and Dictionaries

**Objectives**:
- Creating and manipulating lists, tuples, and dictionaries.
- Basic list methods (append, pop, sort) and dictionary methods.

Hands-on: Create a program to store and retrieve contact information using a dictionary.

### Lesson 8: File Input/Output

**Objectives**:
- Reading from and writing to files.
- Handling file paths and managing file exceptions.

Hands-on: Build a program that reads a file, processes the text (counting words or lines), and writes output to a new file.

### Lesson 9: Error Handling and Exceptions

**Objectives**:
- Try, except, finally for error handling.
- Raising exceptions and using custom exceptions.

Hands-on: Create a simple program with input validation that handles errors gracefully.

### Lesson 10: Object-Oriented Programming (OOP) Basics

**Objectives**:
- Introduction to classes and objects.
- Defining methods, constructors, and instance variables.
- Inheritance and polymorphism.

Hands-on: Build a simple class-based project (e.g., a library system where you can add and lend books).

## Intermediate Python Concepts

### Lesson 11: Working with Libraries and APIs

**Objectives**:
- Installing and using third-party libraries (e.g., requests, pandas).
- Making HTTP requests and processing JSON.

Hands-on: Use an API to fetch and display weather data.

### Lesson 12: Regular Expressions

**Objectives**:
- Using the re library for pattern matching.
- Search, match, findall, and replace using regular expressions.

Hands-on: Write a program that searches for valid email addresses in a text file.

### Lesson 13: Working with Databases (SQLite)

**Objectives**:
- Introduction to SQL and database operations in Python.
- Connecting to a database, creating tables, and performing CRUD operations.

Hands-on: Build a simple CRUD application to manage a to-do list using SQLite.

## Advanced Python Programming

### Lesson 14: Python Generators and Decorators

**Objectives**:
- Understanding and using generators (yield).
- Writing and applying decorators to functions.

Hands-on: Write a custom decorator to time the execution of functions and a generator to iterate over large datasets.

### Lesson 15: Multithreading and Multiprocessing

**Objectives**:
- Introduction to threading and the Global Interpreter Lock (GIL).
- Using the threading and multiprocessing libraries for concurrent execution.

Hands-on: Create a multi-threaded downloader or simple parallel data processing pipeline.

### Lesson 16: Testing and Debugging

**Objectives**:
- Writing unit tests using the unittest framework.
- Using pdb for debugging Python code.

Hands-on: Add unit tests to a previously written program and use the debugger to inspect code execution.

## Project-Based Learning

### Lesson 17: Build a Command-Line Application

**Objectives**:
- Using the argparse library to build CLI programs.
- Packaging Python code and creating executable scripts.

Hands-on: Build a command-line tool (e.g., a file renamer or downloader).

### Lesson 18: Web Development with Flask/Django

**Objectives**:
- Introduction to Flask or Django for web development.
- Routing, templates, and handling form data.

Hands-on: Create a simple web app with user authentication and a basic dashboard.

## Capstone Project

### Lesson 19-20: Final Project

**Objectives**:
- Apply learned concepts to build a complete project from scratch.
- Incorporate file handling, data structures, API interactions, and OOP.

Hands-on: Choose a project such as a personal finance manager, blog engine, or chat application.

