# utils.py

# --- helper functions for input validation

def get_nonempty_string(prompt):
    """prompt user until a non-empty string is provided"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("input cannot be empty")

def get_positive_int(prompt):
    """prompt user until a positive integer is provided"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("value must be positive")
        except ValueError:
            print("invalid input, enter a number")