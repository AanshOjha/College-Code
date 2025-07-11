input_str = input("Enter the string!!!\n")
alpha_count = 0
digit_count = 0
spaces = 0

for char in input_str:
    if char.isalpha():
        alpha_count+=1

    if char.isdigit():
        digit_count+=1
    
    if char==' ':
        spaces+=1
    
with open("char_count.txt", 'w') as file:
    file.write(f"No. of alphabets: {alpha_count}\n")
    file.write(f"No. of digits: {digit_count}\n")
    file.write(f"No. of spaces: {spaces}")

with open("char_count.txt", 'r') as file:
    print(file.read())