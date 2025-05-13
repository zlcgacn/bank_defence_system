# The Bank Defence System

## Project Overview

This project implements a simple command-line based bank account management system using Python. It simulates basic banking operations like creating an account, depositing funds (referred to as "saving" in the code), withdrawing funds, and viewing the current account balance. The system interacts with the user through text prompts and provides feedback on transactions.

It is designed to be a straightforward example of object-oriented programming principles in Python, including class definition, instance attributes, methods, and basic input/output handling. It also includes a suite of unit tests to ensure the core logic functions correctly.

## File Structure and Functionality

This project consists of two primary Python files:

1.  **`project.py`**: This is the main application file containing the core logic for the bank account system.
    *   **`Bank_defence` Class**: This class serves as the blueprint for bank accounts. 
        *   `__init__(self, name, defence=0)`: The constructor initializes a new bank account object. It takes the account holder's `name` and an optional initial `defence` (balance), defaulting to 0. It stores these as instance attributes `self.name_prop` and `self.balance`.
        *   `__str__(self)`: Defines the string representation of a `Bank_defence` object, returning a user-friendly format showing the username and current balance (e.g., "User: TestUser , Defence: 100").
        *   `chooce_serve(self)`: Prompts the user to choose a service ("save" or "withdraw", including abbreviations "s" and "w") and validates the input, looping until a valid choice is entered.
        *   `process_transaction(self, serve)`: Acts as a dispatcher based on the service chosen by the user. It calls either `save_money()` or `withdraw_money()` accordingly and returns the result message from those methods.
        *   `save_money(self)`: Handles the deposit logic. It prompts the user for the amount to save, validates that the input is a non-negative number, updates the account balance, and returns a confirmation message including the new balance.
        *   `withdraw_money(self)`: Handles the withdrawal logic. It prompts the user for the amount to withdraw, performs multiple checks (non-negative amount, sufficient funds, valid numeric input), updates the balance if valid, and returns an appropriate message (confirmation, insufficient funds, or invalid input).
    *   **`main()` Function**: This standalone function orchestrates the main user interaction flow. It handles:
        *   Getting the username from the user with input validation.
        *   Creating an instance of the `Bank_defence` class.
        *   Running the main transaction loop, allowing the user to perform multiple deposits or withdrawals.
        *   Calling the appropriate methods on the `bank_account` object (`chooce_serve`, `process_transaction`).
        *   Displaying transaction results and the updated account status after each operation.
        *   Asking the user if they want to perform another operation and validating their "yes/no" response (accepting 'y', 'ye', 'n' as well).
        *   Exiting gracefully with a thank you message.
        *   **`if __name__ == "__main__":` Block**: This standard Python construct ensures that the `main()` function is called only when the script is executed directly (not when imported as a module).

2.  **`test_project.py`**: This file contains unit tests for `project.py` written using the `pytest` framework style.
    *   **Purpose**: To verify the correctness of the individual components (methods) of the `Bank_defence` class in isolation.
    *   **Framework**: Uses `pytest` conventions (test functions like `test_save_money_valid`, plain `assert` statements for checks) for clarity and conciseness.
    *   **Mocking**: Leverages `unittest.mock.patch` to simulate user input (`builtins.input`) during tests. This prevents tests from actually pausing and waiting for user interaction, allowing them to run automatically and predictably. `patch` is also used to check if expected print messages (like error messages in `chooce_serve`) are called.
    *   **Coverage**: Tests cover various scenarios, including:
        *   Correct initialization of account name and balance.
        *   Accurate string representation (`__str__`).
        *   Valid and invalid (negative, non-numeric) deposit attempts.
        *   Valid and invalid (negative, non-numeric, insufficient funds) withdrawal attempts.
        *   Correct dispatching logic in `process_transaction` for both "save"/"s" and "withdraw"/"w".
        *   Input validation loop in `chooce_serve`.

## Design Choices and Rationale

Several design decisions were made during the development of this system:

*   **Object-Oriented Approach**: Using a `Bank_defence` class was chosen to encapsulate the data (account name, balance) and the operations (save, withdraw) related to a single bank account. This promotes modularity, makes the code easier to understand and maintain, and allows for potential future expansion (e.g., adding different account types) compared to using only procedural functions and global variables.
*   **Error Handling**: Instead of letting the program crash on invalid user input (e.g., entering text when a number is expected for an amount), `try-except ValueError` blocks are used in `save_money` and `withdraw_money`. Specific checks for negative amounts and insufficient funds are also included. These methods return user-friendly error messages rather than raising exceptions directly to the main loop, providing a smoother user experience.
*   **User Interaction Flow**: The `main()` function implements clear loops for getting validated user input for the username, service choice, and the decision to continue or exit. This ensures the user is guided through the process and invalid inputs are handled gracefully by prompting again.
*   **Separation of Concerns**: The `process_transaction` method acts as a simple dispatcher, separating the logic of *choosing* a service from the logic of *executing* the deposit or withdrawal. Furthermore, moving the main application flow into a dedicated `main()` function, separate from the class definition, improves code organization.
*   **Testing Strategy**: Unit testing with `pytest` was adopted to ensure the reliability of the core banking logic. Using `mock.patch` was crucial to isolate the tests from external dependencies like user input, making the tests deterministic and fast. Testing individual methods helps catch bugs early and provides confidence when refactoring or adding new features.
*   **Method Return Values**: Transaction methods (`save_money`, `withdraw_money`, `process_transaction`) were designed to return status/result messages instead of directly printing them. This allows the calling code (`main()` function or test functions) to decide how to present this information, improving testability (tests can assert the returned message) and flexibility.

## How to Run

1.  **Run the Application**: Navigate to the project directory in your terminal and execute:
    ```bash
    python3 project.py
    ```
    Follow the on-screen prompts to interact with the bank system.

2.  **Run the Tests**: Ensure you have `pytest` installed (`python3 -m pip install pytest`). Navigate to the project directory and run:
    ```bash
    pytest
    ```
    or, if the `pytest` command is not in your PATH:
    ```bash
    python3 -m pytest
    ```
    This will automatically discover and run the tests in `test_project.py`.

## Video Demo

[Project Demo Video](https://www.youtube.com/watch?v=hIf50gvpSkc&ab_channel=%E6%9D%B1%E9%A2%A8%E7%A5%9E) 
(https://img.youtube.com/vi/hIf50gvpSkc&ab_channel=東風神/0.jpg)](https://www.youtube.com/watch?v=hIf50gvpSkc&ab_channel=東風神)
