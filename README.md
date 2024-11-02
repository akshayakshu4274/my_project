# my_project

# Project Overview

This project contains three programs:
1. **Word Frequency**: Computes the frequency of words in a given line of text.
2. **Circular Queue**: Implements a circular queue with a fixed maximum length.
3. **Password Validator**: Validates passwords based on specified criteria.

## Usage
- Run the `main.py` script to execute all programs concurrently.
- Modify `inputs/input.txt` to change input text for word frequency.

## Running Tests
- Unit tests are available in the `tests/` directory.
- Run tests with the command:
  ```bash
  pytest tests/

## Project Directory Structure
my_project/
├── .github/
│   └── workflows/
│       └── python-app.yml         # GitHub Actions workflow for automated testing
├── inputs/
│   └── input.txt                  # Text file for word frequency input data
├── src/
│   ├── word_frequency.py          # Word frequency program
│   ├── circular_queue.py          # Circular queue implementation
│   ├── password_validator.py      # Password validation program
│   └── main.py                    # Main file to run all programs concurrently
├── tests/
│   ├── test_word_frequency.py     # Unit test for word frequency program
│   ├── test_circular_queue.py     # Unit test for circular queue
│   └── test_password_validator.py # Unit test for password validation
└── README.md                      # README file with project instructions
