import re

def check_password_strength(password: str) -> str:
    """
    Check the strength of a given password.
    Returns: Weak, Medium, or Strong
    """
    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Scoring
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = errors.count(False)

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print("Password strength:", check_password_strength(pwd))
