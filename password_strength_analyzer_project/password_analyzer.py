import re
import secrets
import string

COMMON = {"password","123456","qwerty","admin","welcome"}

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    checks = [
        (r"[A-Z]", "Add uppercase letters"),
        (r"[a-z]", "Add lowercase letters"),
        (r"\d", "Add numbers"),
        (r"[!@#$%^&*(),.?\":{}|<>]", "Add special characters")
    ]

    for pattern, advice in checks:
        if re.search(pattern, password):
            score += 1
        else:
            feedback.append(advice)

    if password.lower() in COMMON:
        score = max(0, score - 4)
        feedback.append("Avoid common passwords")

    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, feedback

if __name__ == "__main__":
    pwd = input("Enter password: ")
    score, strength, feedback = analyze_password(pwd)

    print(f"Score: {score}/10")
    print("Strength:", strength)

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print("-", f)

        print("\nGenerated secure password:")
        print(generate_password())