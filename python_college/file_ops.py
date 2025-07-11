with open("students.txt", 'a+') as file:
    file.seek(0)
    text = file.read()
    print(text[-8:-1])
    # file.seek(0, 2)
    # content = file.write(text)
    # print(content)