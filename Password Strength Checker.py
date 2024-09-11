import re

def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password)
    lower_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Strength calculation
    strength = 0
    if length_criteria:
        strength += 1
    if upper_criteria:
        strength += 1
    if lower_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_criteria:
        strength += 1

    # Password strength evaluation
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Medium"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")
