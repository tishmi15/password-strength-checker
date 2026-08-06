import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if re.search(r"[A-Z]", password):
        strength += 1

    if re.search(r"[a-z]", password):
        strength += 1

    if re.search(r"\d", password):
        strength += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 5:
        return "Very Strong Password"
    elif strength == 4:
        return "Strong Password"
    elif strength == 3:
        return "Medium Password"
    else:
        return "Weak Password"

password = input("Enter your password: ")
result = check_password_strength(password)

print("\nPassword Strength:", result)