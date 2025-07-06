# Python Exceptions - Task 0: Safe List Printing

This project is part of the ALU Higher Level Programming module.  
The goal of this task is to safely print elements from a list using Python exception handling.

## Files

- **0-safe_print_list.py**  
  Contains the `safe_print_list(my_list=[], x=0)` function, which prints `x` elements from a list. It uses `try` / `except` blocks to handle cases where `x` is greater than the actual length of the list. It does **not** use `len()` or any imports.

- **0-main.py**  
  A test script that imports and calls the function with different values of `x`.

## Usage

To test the function, run:

```bash
./0-main.py

