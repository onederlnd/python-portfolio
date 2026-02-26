# utils.py
import datetime

# --- helper functions for input validation

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

def parse_date(date_str):
    """parse a date in mm/dd/yyyy format, default to today"""
    if not date_str.strip():
        return datetime.date.today()
    try:
        return datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
    except ValueError:
        print("invalid format, using today's date")
        return datetime.date.today()