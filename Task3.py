import re
def Check_password(password):

    strength = 0

    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 5:
        remarks = "very Strong password"
    elif strength == 4:
        remarks = "Strong password"
    elif strength == 3:
        remarks = "Moderate password"
    elif strength == 2:
        remarks = "Weak password"
    else:
        remarks = "Very Week"

    return strength, remarks    

#main Program

print("Password Strength Checker")

password = input("Enter your password: ")

strength, feedback = Check_password(password)

print(f"\n Score : {strength}/5")
print(f" Strength : {feedback}")