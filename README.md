## Introduction
This repository contains a simple Python script to verify email addresses using regular expressions (regex). The script checks if the provided email address matches the pattern and verifies its validity.

## Installation
To use this script, you need to have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/seenumehta/Email-verify-using-REGEX.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd Email-verify-using-REGEX
    ```
3. Run the script:
    ```bash
    python main.py
    ```

## Code Explanation
The `emailVerify` function uses regex to validate the email address. The pattern used is:
```python
r'^[a-z0-9]+[\._]?[a-z0-9]+[@][a-z]+[.][a-z]{2,3}$'
```
The function checks for:
- Lowercase letters (a-z)
- Digits (0-9)
- Optional periods (.) and underscores (_)
- A mandatory "@" symbol
- A domain name followed by a period (.)
- A domain suffix of 2 to 3 characters


