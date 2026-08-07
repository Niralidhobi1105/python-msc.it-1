password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False
repeated = False

special_chars = "`~!@#$%^&*()_-<>?/|,.;:'{[]}\""

for i in range(len(password)):
    ch = password[i]

    if ch.isupper():
        upper = True

    elif ch.islower():
        lower = True

    elif ch.isdigit():
        digit = True

    elif ch in special_chars:
        special = True

    # Check consecutive repeated characters
    if i > 0 and password[i] == password[i - 1]:
        repeated = True


print("\nPassword Strength Analyzer:")
print("Upper case letter:", upper)
print("Lower case letter:", lower)
print("Digit:", digit)
print("Special character:", special)
print("Repeated consecutive character:", repeated)
