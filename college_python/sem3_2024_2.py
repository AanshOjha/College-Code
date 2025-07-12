# def removenth(s: str, n):
#     if n<0:
#         return "invalid"
#     if n>len(s):
#         return s
#     else:
#         return s[:n]+s[n+1:]
    
# print(removenth("STRING", 4))

def commas(s:str):
    words = s.split(",")
    words = [word.strip() for word in words]

    words.sort()
    print(words)
    return ",".join(words)

print(commas("without, hello, bag, world "))


def is_valid_password(password):
    # Check password length
    if len(password) < 6 or len(password) > 12:
        return False

    # Initialize required flags
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    # Check each character
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in '$#@':
            has_special = True

    # Return True only if all conditions are met
    return has_lower and has_upper and has_digit and has_special


# Taking input from user
passwords = input("Enter passwords separated by commas: ").split(",")

# Filter and print valid passwords
valid_passwords = [pwd.strip() for pwd in passwords if is_valid_password(pwd.strip())]

print(",".join(valid_passwords))


