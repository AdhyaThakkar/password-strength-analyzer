import math
# HashSet for O(1) breach lookup
breached = {"password", "123456", "qwerty", "letmein", "admin",
            "welcome", "monkey", "dragon", "iloveyou", "sunshine"}

# list to track last 5 passwords (history)
history = []

def analyze(pwd):
    upper   = [c for c in pwd if c.isupper()]
    lower   = [c for c in pwd if c.islower()]
    digits  = [c for c in pwd if c.isdigit()]
    special = [c for c in pwd if c in "!@#$%^&*()_+-=[]{}|;:,.<>?"]

    score = 0
    if len(pwd) >= 12:   score += 40
    elif len(pwd) >= 8:  score += 20
    else:                score += 10
    if len(upper) > 0:   score += 15
    if len(lower) > 0:   score += 15
    if len(digits) > 0:  score += 15
    if len(special) > 0: score += 15
    is_breached = pwd.lower() in breached  # set lookup
    if is_breached:
        score = 10
    # entropy = length * log2(possible charset size)
    charset = (26 if len(lower) > 0 else 0) + (26 if len(upper) > 0 else 0) \
            + (10 if len(digits) > 0 else 0) + (32 if len(special) > 0 else 0)
    entropy = round(len(pwd) * math.log2(charset), 2) if charset > 0 else 0

    return len(pwd), len(upper), len(lower), len(digits), len(special), is_breached, score, entropy

def get_suggestions(length, upper, lower, digits, special, is_breached):
    tips = []  # list to collect suggestions
    if length < 12:    tips.append("Use at least 12 characters")
    if upper == 0:     tips.append("Add uppercase letters (A-Z)")
    if lower == 0:     tips.append("Add lowercase letters (a-z)")
    if digits == 0:    tips.append("Include a number (0-9)")
    if special == 0:   tips.append("Add a special character like !@#$%")
    if is_breached:    tips.append("Too common - pick something unique!")
    return tips[:3]

def main():
    print("=== Password Strength Analyzer ===\n")
    while True:
        print("1. Check a password\n2. View history\n3. Quit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            pwd = input("Enter a password: ").strip()
            length, upper, lower, digits, special, is_breached, score, entropy = analyze(pwd)
            label = "Strong" if score >= 70 else "Medium" if score >= 40 else "Weak"
            elabel = "very hard to crack" if entropy >= 60 else "moderately secure" if entropy >= 40 else "easy to crack"
            print(f"\nScore: {score}/100 - {label}")
            print(f"Entropy: {entropy} bits ({elabel})")
            print(f"Length: {length} | Upper: {upper} | Lower: {lower} | Digits: {digits} | Special: {special}")

            tips = get_suggestions(length, upper, lower, digits, special, is_breached)
            if len(tips) > 0:
                print("Suggestions:")
                for i in range(len(tips)):
                    print(f"  {i+1}. {tips[i]}")
            else:
                print("Great password! No suggestions.")

            # add to history, keep only last 5
            history.append(pwd)
            if len(history) > 5:
                history.pop(0)
            print("-" * 38 + "\n")

        elif choice == "2":
            if len(history) == 0:
                print("No passwords checked yet.\n")
            else:
                print(f"\nLast {len(history)} password(s):")
                for i in range(len(history)):
                    print(f"  {i+1}. {history[i]}")
                print()

        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid option, try again.\n")
main()
