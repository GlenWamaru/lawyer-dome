# helpers.py
import re

def validate_email(email):
    # Simple email validation using regex
    pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    return re.match(pattern, email)

def validate_phone_number(phone_number):
    # Simple phone number validation using regex
    pattern = r"^\d{10}$"
    return re.match(pattern, phone_number)
