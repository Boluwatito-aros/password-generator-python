import random
import string

"""
A strong password must have between 12 and 16 characters,
upper and lower case letters, numbers, symbols,
and must not match the username.
"""

s_letter = list(string.ascii_lowercase)
b_letter = list(string.ascii_uppercase)
nums = list(string.digits)
chars = list(string.punctuation)
ultimate = s_letter + b_letter + nums + chars

username = input("Enter your username: ")

def generate_password():
    # Guarantee at least one of each character type
    pass_w = [
        random.choice(s_letter),
        random.choice(b_letter),
        random.choice(nums),
        random.choice(chars)
    ]
    length = random.randint(12, 16)
    for i in range(length - 4):  # Fix: was length - 2, leaving password short by 2
        pass_w.append(random.choice(ultimate))  # Fix: was += which adds characters individually as strings
    random.shuffle(pass_w)
    return ''.join(pass_w)

def evaluate_strength(password):
    """Score the password against common security criteria."""
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    if any(c in string.ascii_lowercase for c in password):
        score += 1
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    if any(c in string.digits for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 5:
        feedback = "Strong"
    elif score >= 3:
        feedback = "Moderate"
    else:
        feedback = "Weak"

    return f"Password strength: {feedback} ({score}/5)"

while True:
    password = generate_password()
    if password != username:
        break

print(f"Your generated password is: {password}")
print(evaluate_strength(password))